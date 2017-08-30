# coding=utf-8
# Copyright 2017 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for creating Sparsely-Gated Mixture-of-Experts Layers.

See "Outrageously Large Neural Networks"
https://arxiv.org/abs/1701.06538
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

# Dependency imports

import six
from six.moves import xrange  # pylint: disable=redefined-builtin
from six.moves import zip  # pylint: disable=redefined-builtin
import tensorflow as tf

from tensorflow.python.framework import function

DEFAULT_DEV_STRING = "existing_device"


@function.Defun(
    python_grad_func=lambda x, dy: tf.convert_to_tensor(dy),
    shape_func=lambda op: [op.inputs[0].get_shape()])
def convert_gradient_to_tensor(x):
  """Identity operation whose gradient is converted to a `Tensor`.

  Currently, the gradient to `tf.concat` is particularly expensive to
  compute if dy is an `IndexedSlices` (a lack of GPU implementation
  forces the gradient operation onto CPU).  This situation occurs when
  the output of the `tf.concat` is eventually passed to `tf.gather`.
  It is sometimes faster to convert the gradient to a `Tensor`, so as
  to get the cheaper gradient for `tf.concat`.  To do this, replace
  `tf.concat(x)` with `convert_gradient_to_tensor(tf.concat(x))`.

  Args:
    x: A `Tensor`.

  Returns:
    The input `Tensor`.
  """
  return x


class Parallelism(object):
  """Helper class for creating sets of parallel function calls.

  The purpose of this class is to replace this code:

      e = []
      f = []
      for i in xrange(len(devices)):
        with tf.device(devices[i]):
          e_, f_ = func(a[i], b[i], c)
          e.append(e_)
          f.append(f_)

  with this code:

      e, f = expert_utils.Parallelism(devices)(func, a, b, c)
  """

  def __init__(self,
               device_names_or_functions,
               reuse=None,
               caching_devices=None,
               daisy_chain_variables=False):
    """Create a Parallelism.

    Args:
      device_names_or_functions: A list of length n, containing device names
        or device functions (see `tf.device`)
      reuse: True or None.  Whether to reuse variables created in the first
        replica in the subsequent replicas.
      caching_devices: Either `None`, or a list of length n containing device
        names.
      daisy_chain_variables: a boolean - if true, then copies variables in a
        daisy chain between devices.

    Returns:
      a Parallelism.
    """
    assert device_names_or_functions
    self._devices = device_names_or_functions
    self._n = len(device_names_or_functions)
    self._reuse = reuse
    self._caching_devices = self._maybe_repeat(caching_devices)
    self._daisy_chain_variables = daisy_chain_variables

  def __call__(self, fn, *args, **kwargs):
    """A parallel set of function calls (using the specified devices).

    Args:
      fn: a function or a list of n functions.
      *args: additional args.  Each arg should either be not a list, or a list
         of length n.
      **kwargs: additional keyword args.  Each arg should either be not a
         list, or a list of length n.

    Returns:
      either a single list of length n (if fn does not return a tuple), or a
      tuple of lists of length n (if fn returns a tuple).
    """
    # Construct lists or args and kwargs for each function.
    if args:
      my_args = transpose_list_of_lists(
          [self._maybe_repeat(arg) for arg in args])
    else:
      my_args = [[] for _ in xrange(self.n)]
    my_kwargs = [{} for _ in xrange(self.n)]
    for k, v in six.iteritems(kwargs):
      vals = self._maybe_repeat(v)
      for i in xrange(self.n):
        my_kwargs[i][k] = vals[i]

    # Construct lists of functions.
    fns = self._maybe_repeat(fn)

    # Now make the parallel call.
    outputs = []
    cache = {}
    for i in xrange(self.n):

      def daisy_chain_getter(getter, name, *args, **kwargs):
        """Get a variable and cache in a daisy chain."""
        device_var_key = (self._devices[i], name)
        if device_var_key in cache:
          # if we have the variable on the correct device, return it.
          return cache[device_var_key]
        if name in cache:
          # if we have it on a different device, copy it from the last device
          v = tf.identity(cache[name])
        else:
          var = getter(name, *args, **kwargs)
          v = tf.identity(var._ref())  # pylint: disable=protected-access
        # update the cache
        cache[name] = v
        cache[device_var_key] = v
        return v

      # Variable scope will not reset caching_device on reused variables,
      # so we make a custom getter that uses identity to cache the variable.
      # pylint: disable=cell-var-from-loop
      def caching_getter(getter, name, *args, **kwargs):
        v = getter(name, *args, **kwargs)
        key = (self._caching_devices[i], name)
        if key in cache:
          return cache[key]
        with tf.device(self._caching_devices[i]):
          ret = tf.identity(v._ref())  # pylint: disable=protected-access
        cache[key] = ret
        return ret

      if self._daisy_chain_variables:
        custom_getter = daisy_chain_getter
      elif self._caching_devices[i]:
        custom_getter = caching_getter
      else:
        custom_getter = None
      # pylint: enable=cell-var-from-loop
      with tf.name_scope("parallel_%d" % i):
        with tf.variable_scope(
            tf.get_variable_scope() if self._reuse else "parallel_%d" % i,
            reuse=True if i > 0 and self._reuse else None,
            caching_device=self._caching_devices[i],
            custom_getter=custom_getter):
          # TODO(noam, epot, avaswani)
          # Allows for passing no device in case you want to default to the
          # existing device. This is needed when we put all experts on a single
          # device, for example in local_moe.
          if self._devices[i] != DEFAULT_DEV_STRING:
            with tf.device(self._devices[i]):
              outputs.append(fns[i](*my_args[i], **my_kwargs[i]))
          else:
            outputs.append(fns[i](*my_args[i], **my_kwargs[i]))
    if isinstance(outputs[0], tuple):
      outputs = list(zip(*outputs))
      outputs = tuple([list(o) for o in outputs])
    return outputs

  @property
  def n(self):
    return self._n

  @property
  def devices(self):
    return self._devices

  def _maybe_repeat(self, x):
    """Utility function for processing arguments that are singletons or lists.

    Args:
      x: either a list of self.n elements, or not a list.

    Returns:
      a list of self.n elements.
    """
    if isinstance(x, list):
      assert len(x) == self.n
      return x
    else:
      return [x] * self.n


def _rowwise_unsorted_segment_sum(values, indices, n):
  """UnsortedSegmentSum on each row.

  Args:
    values: a `Tensor` with shape `[batch_size, k]`.
    indices: an integer `Tensor` with shape `[batch_size, k]`.
    n: an integer.
  Returns:
    A `Tensor` with the same type as `values` and shape `[batch_size, n]`.
  """
  batch, k = tf.unstack(tf.shape(indices), num=2)
  indices_flat = tf.reshape(indices, [-1]) + tf.div(tf.range(batch * k), k) * n
  ret_flat = tf.unsorted_segment_sum(
      tf.reshape(values, [-1]), indices_flat, batch * n)
  return tf.reshape(ret_flat, [batch, n])


def _normal_distribution_cdf(x, stddev):
  """Evaluates the CDF of the normal distribution.

  Normal distribution with mean 0 and standard deviation stddev,
  evaluated at x=x.

  input and output `Tensor`s have matching shapes.

  Args:
    x: a `Tensor`
    stddev: a `Tensor` with the same shape as `x`.

  Returns:
    a `Tensor` with the same shape as `x`.

  """
  return 0.5 * (1.0 + tf.erf(x / (math.sqrt(2) * stddev + 1e-20)))


def _prob_in_top_k(
    clean_values, noisy_values, noise_stddev, noisy_top_values, k):
  """Helper function to NoisyTopKGating.

  Computes the probability that value is in top k, given different random noise.

  This gives us a way of backpropagating from a loss that balances the number
  of times each expert is in the top k experts per example.

  In the case of no noise, pass in None for noise_stddev, and the result will
  not be differentiable.

  Args:
    clean_values: a `Tensor` of shape [batch, n].
    noisy_values: a `Tensor` of shape [batch, n].  Equal to clean values plus
      normally distributed noise with standard deviation noise_stddev.
    noise_stddev: a `Tensor` of shape [batch, n], or None
    noisy_top_values: a `Tensor` of shape [batch, m].
       "values" Output of tf.top_k(noisy_top_values, m).  m >= k+1
    k: an integer.

  Returns:
    a `Tensor` of shape [batch, n].
  """
  batch = tf.shape(clean_values)[0]
  m = tf.shape(noisy_top_values)[1]
  top_values_flat = tf.reshape(noisy_top_values, [-1])
  # we want to compute the threshold that a particular value would have to
  # exceed in order to make the top k.  This computation differs depending
  # on whether the value is already in the top k.
  threshold_positions_if_in = tf.range(batch) * m + k
  threshold_if_in = tf.expand_dims(
      tf.gather(top_values_flat, threshold_positions_if_in), 1)
  is_in = tf.greater(noisy_values, threshold_if_in)
  if noise_stddev is None:
    return tf.to_float(is_in)
  threshold_positions_if_out = threshold_positions_if_in - 1
  threshold_if_out = tf.expand_dims(
      tf.gather(top_values_flat, threshold_positions_if_out), 1)
  # is each value currently in the top k.
  prob_if_in = _normal_distribution_cdf(clean_values - threshold_if_in,
                                        noise_stddev)
  prob_if_out = _normal_distribution_cdf(clean_values - threshold_if_out,
                                         noise_stddev)
  prob = tf.where(is_in, prob_if_in, prob_if_out)
  return prob


def cv_squared(x):
  """The squared coefficient of variation of a sample.

  Useful as a loss to encourage a positive distribution to be more uniform.
  Epsilons added for numerical stability.
  Returns 0 for an empty Tensor.

  Args:
    x: a `Tensor`.

  Returns:
    a `Scalar`.
  """
  epsilon = 1e-10
  float_size = tf.to_float(tf.size(x)) + epsilon
  mean = tf.reduce_sum(x) / float_size
  variance = tf.reduce_sum(tf.square(x - mean)) / float_size
  return variance / (tf.square(mean) + epsilon)


def _gates_to_load(gates):
  """Compute the true load per expert, given the gates.

  The load is the number of examples for which the corresponding gate is >0.

  Args:
    gates: a `Tensor` of shape [batch_size, n]
  Returns:
    a float32 `Tensor` of shape [n]
  """
  return tf.reduce_sum(tf.to_float(gates > 0), 0)


def _my_top_k(x, k):
  """GPU-compatible version of top-k that works for very small constant k.

  Calls argmax repeatedly.

  tf.nn.top_k is implemented for GPU, but the gradient, sparse_to_dense,
  seems not to be, so if we use tf.nn.top_k, then both the top_k and its
  gradient go on cpu.  Once this is not an issue, this function becomes
  obselete and should be replaced by tf.nn.top_k.

  Args:
    x: a 2d Tensor.
    k: a small integer.

  Returns:
    values: a Tensor of shape [batch_size, k]
    indices: a int32 Tensor of shape [batch_size, k]
  """
  if k > 10:
    return tf.nn.top_k(x, k)
  values = []
  indices = []
  depth = tf.shape(x)[1]
  for i in xrange(k):
    values.append(tf.reduce_max(x, 1))
    argmax = tf.argmax(x, 1)
    indices.append(argmax)
    if i + 1 < k:
      x += tf.one_hot(argmax, depth, -1e9)
  return tf.stack(values, axis=1), tf.to_int32(tf.stack(indices, axis=1))


def noisy_top_k_gating(x,
                       num_experts,
                       train,
                       k=2,
                       initializer=tf.zeros_initializer(),
                       noisy_gating=True,
                       noise_epsilon=1e-2,
                       name=None):
  """Noisy top-k gating.

  See paper: https://arxiv.org/abs/1701.06538.

  Args:
    x: input Tensor with shape [batch_size, input_size]
    num_experts: an integer
    train: a boolean - we only add noise at training time.
    k: an integer - number of experts per example
    initializer: an initializer
    noisy_gating: a boolean
    noise_epsilon: a float
    name: an optional string

  Returns:
    gates: a Tensor with shape [batch_size, num_experts]
    load: a Tensor with shape [num_experts]
  """
  with tf.variable_scope(name, default_name="noisy_top_k_gating"):
    input_size = x.get_shape().as_list()[-1]
    w_gate = tf.get_variable(
        "w_gate", [input_size, num_experts], tf.float32, initializer)
    if noisy_gating:
      w_noise = tf.get_variable("w_noise",
                                [input_size, num_experts], tf.float32,
                                initializer)
    clean_logits = tf.matmul(x, w_gate)
    if noisy_gating:
      raw_noise_stddev = tf.matmul(x, w_noise)
      noise_stddev = ((tf.nn.softplus(raw_noise_stddev) + noise_epsilon) *
                      (tf.to_float(train)))
      noisy_logits = clean_logits + (
          tf.random_normal(tf.shape(clean_logits)) * noise_stddev)
      logits = noisy_logits
      if not tf.get_variable_scope().reuse:
        tf.summary.histogram("noisy_logits", noisy_logits)
        tf.summary.histogram("noise_stddev", noise_stddev)
    else:
      logits = clean_logits
    top_logits, top_indices = _my_top_k(logits, min(k + 1, num_experts))
    top_k_logits = tf.slice(top_logits, [0, 0], [-1, k])
    top_k_indices = tf.slice(top_indices, [0, 0], [-1, k])
    top_k_gates = tf.nn.softmax(top_k_logits)
    # This will be a `Tensor` of shape `[batch_size, n]`, with zeros in the
    # positions corresponding to all but the top k experts per example.
    gates = _rowwise_unsorted_segment_sum(top_k_gates, top_k_indices,
                                          num_experts)
    if noisy_gating and k < num_experts:
      load = tf.reduce_sum(
          _prob_in_top_k(clean_logits, noisy_logits, noise_stddev, top_logits,
                         k), 0)
    else:
      load = _gates_to_load(gates)
    if not tf.get_variable_scope().reuse:
      tf.summary.histogram("importance", tf.reduce_sum(gates, 0))
      tf.summary.histogram("load", load)
    return gates, load


class PadRemover(object):
  """Helper to remove padding from a tensor before sending to the experts.

  The padding is computed for one reference tensor containing the padding mask
  and then can be applied to any other tensor of shape [dim_origin,...].

  Ex:
      input = [
        [tok1, tok2],
        [tok3, tok4],
        [0, 0],
        [0, 0],
        [tok5, tok6],
        [0, 0],
      ]
      output = [
        [tok1, tok2],
        [tok3, tok4],
        [tok5, tok6],
      ]
  """

  def __init__(self, pad_mask):
    """Compute and store the location of the padding.

    Args:
      pad_mask (tf.Tensor): Reference padding tensor of shape
        [batch_size,length] or [dim_origin] (dim_origin=batch_size*length)
        containing non-zeros positive values to indicate padding location.
    """
    self.nonpad_ids = None
    self.dim_origin = None

    with tf.name_scope("pad_reduce/get_ids"):
      pad_mask = tf.reshape(pad_mask, [-1])  # Flatten the batch
      # nonpad_ids contains coordinates of zeros rows (as pad_mask is
      # float32, checking zero equality is done with |x| < epsilon, with
      # epsilon=1e-9 as standard, here pad_mask only contains positive values
      # so tf.abs would be redundant)
      self.nonpad_ids = tf.to_int32(tf.where(pad_mask < 1e-9))
      self.dim_origin = tf.shape(pad_mask)[:1]

  def remove(self, x):
    """Remove padding from the given tensor.

    Args:
      x (tf.Tensor): of shape [dim_origin,...]

    Returns:
      a tensor of shape [dim_compressed,...] with dim_compressed <= dim_origin
    """
    with tf.name_scope("pad_reduce/remove"):
      x_shape = x.get_shape().as_list()
      x = tf.gather_nd(
          x,
          indices=self.nonpad_ids,
      )
      # This is a hack but for some reason, gather_nd return a tensor of
      # undefined shape, so the shape is set up manually
      x.set_shape([None] + x_shape[1:])
    return x

  def restore(self, x):
    """Add padding back to the given tensor.

    Args:
      x (tf.Tensor): of shape [dim_compressed,...]

    Returns:
      a tensor of shape [dim_origin,...] with dim_compressed >= dim_origin. The
      dim is restored from the original reference tensor
    """
    with tf.name_scope("pad_reduce/restore"):
      x = tf.scatter_nd(
          indices=self.nonpad_ids,
          updates=x,
          shape=tf.concat([self.dim_origin, tf.shape(x)[1:]], axis=0),
      )
    return x


class SparseDispatcher(object):
  """Helper for implementing a mixture of experts.

  The purpose of this class is to create input minibatches for the
  experts and to combine the results of the experts to form a unified
  output tensor.

  There are two functions:
    dispatch - take an input Tensor and create input Tensors for each expert.
    combine - take output Tensors from each expert and form a combined output
      Tensor.  Outputs from different experts for the same batch element are
      summed together, weighted by the provided "gates".

  The class is initialized with a "gates" Tensor, which specifies which
  batch elements go to which experts, and the weights to use when combining
  the outputs.  Batch element b is sent to expert e iff gates[b, e] != 0.

  The inputs and outputs are all two-dimensional [batch, depth].
  Caller is responsible for collapsing additional dimensions prior to
  calling this class and reshaping the output to the original shape.
  See reshape_like().

  Example use:

  gates: a float32 `Tensor` with shape `[batch_size, num_experts]`
  inputs: a float32 `Tensor` with shape `[batch_size, input_size]`
  experts: a list of length `num_experts` containing sub-networks.

    dispatcher = SparseDispatcher(num_experts, gates)
    expert_inputs = dispatcher.dispatch(inputs)
    expert_outputs = [experts[i](expert_inputs[i]) for i in range(num_experts)]
    outputs = dispatcher.combine(expert_outputs)

  The preceding code sets the output for a particular example b to:
  output[b] = Sum_i(gates[b, i] * experts[i](inputs[b]))

  This class takes advantage of sparsity in the gate matrix by including in the
  `Tensor`s for expert i only the batch elements for which `gates[b, i] > 0`.
  """

  def __init__(self, num_experts, gates):
    """Create a SparseDispatcher.

    Args:
      num_experts: an integer.
      gates: a `Tensor` of shape `[batch_size, num_experts]`.

    Returns:
      a SparseDispatcher
    """
    self._gates = gates
    self._num_experts = num_experts

    where = tf.to_int32(tf.where(tf.transpose(gates) > 0))
    self._expert_index, self._batch_index = tf.unstack(where, num=2, axis=1)
    self._part_sizes_tensor = tf.reduce_sum(tf.to_int32(gates > 0), [0])
    self._nonzero_gates = tf.gather(
        tf.reshape(self._gates, [-1]),
        self._batch_index * num_experts + self._expert_index)

  def dispatch(self, inp):
    """Create one input Tensor for each expert.

    The `Tensor` for a expert `i` contains the slices of `inp` corresponding
    to the batch elements `b` where `gates[b, i] > 0`.

    Args:
      inp: a `Tensor` of shape "[batch_size, <extra_input_dims>]`
    Returns:
      a list of `num_experts` `Tensor`s with shapes
        `[expert_batch_size_i, <extra_input_dims>]`.
    """
    inp = tf.gather(inp, self._batch_index)
    return tf.split(inp, self._part_sizes_tensor, 0)

  def combine(self, expert_out, multiply_by_gates=True):
    """Sum together the expert output, weighted by the gates.

    The slice corresponding to a particular batch element `b` is computed
    as the sum over all experts `i` of the expert output, weighted by the
    corresponding gate values.  If `multiply_by_gates` is set to False, the
    gate values are ignored.

    Args:
      expert_out: a list of `num_experts` `Tensor`s, each with shape
        `[expert_batch_size_i, <extra_output_dims>]`.
      multiply_by_gates: a boolean

    Returns:
      a `Tensor` with shape `[batch_size, <extra_output_dims>]`.
    """
    # see comments on convert_gradient_to_tensor
    stitched = convert_gradient_to_tensor(tf.concat(expert_out, 0))
    if multiply_by_gates:
      stitched *= tf.expand_dims(self._nonzero_gates, 1)
    combined = tf.unsorted_segment_sum(stitched, self._batch_index,
                                       tf.shape(self._gates)[0])
    return combined

  def expert_to_gates(self):
    """Gate values corresponding to the examples in the per-expert `Tensor`s.

    Returns:
      a list of `num_experts` one-dimensional `Tensor`s with type `tf.float32`
          and shapes `[expert_batch_size_i]`
    """
    return tf.split(self._nonzero_gates, self._part_sizes_tensor, 0)

  @property
  def part_sizes(self):
    return self._part_sizes_tensor


class DistributedSparseDispatcher(object):
  """A distributed version of SparseDispatcher.

  Instead of one batch of input examples, we simultaneously process
  a list of num_datashards batches of input examples.  The per-expert
  `Tensor`s contain a combination of examples from the different datashards.

  Each datashard is associated with a particular device and each expert is
  associated with a particular device.  All per-datashard and per-expert
  `Tensor`s are created on those devices.  There is no single-device bottleneck.
  """

  def __init__(self, data_parallelism, expert_parallelism, gates):
    """Create a DistributedSparseDispatcher.

    Args:
      data_parallelism: a Parallelism object.
      expert_parallelism: a Parallelism object.
      gates: a list of datashard_parallelism.n `Tensor`s of shapes
        `[batch_size[d], num_experts]`.

    Returns:
      a DistributedSparseDispatcher
    """
    self._gates = gates
    self._dp = data_parallelism
    self._ep = expert_parallelism
    assert len(gates) == self._dp.n
    self._dispatchers = self._dp(SparseDispatcher, self._ep.n, gates)

  def dispatch(self, inp):
    """Create one input Tensor for each expert.

    Args:
      inp: a list of length num_datashards `Tensor`s with shapes
        `[batch_size[d], <extra_input_dims>]`.
    Returns:
      a list of `num_experts` `Tensor`s with shapes
        `[num_examples[i], <extra_input_dims>]`.
    """
    dispatched = self._dp(lambda a, b: a.dispatch(b), self._dispatchers, inp)
    ret = self._ep(tf.concat, transpose_list_of_lists(dispatched), 0)
    if ret[0].dtype == tf.float32:
      # see comments on convert_gradient_to_tensor
      ret = self._ep(convert_gradient_to_tensor, ret)
    return ret

  def combine(self, expert_out, multiply_by_gates=True):
    """Sum together the expert output, multiplied by the corresponding gates.

    Args:
      expert_out: a list of `num_experts` `Tensor`s, each with shape
        `[expert_batch_size_i, <extra_output_dims>]`.
      multiply_by_gates: a boolean.

    Returns:
      a list of num_datashards `Tensor`s with shapes
        `[batch_size[d], <extra_output_dims>]`.
    """
    expert_part_sizes = tf.unstack(
        tf.stack([d.part_sizes for d in self._dispatchers]),
        num=self._ep.n,
        axis=1)
    # list of lists of shape [num_experts][num_datashards]
    expert_output_parts = self._ep(tf.split, expert_out, expert_part_sizes)
    expert_output_parts_t = transpose_list_of_lists(expert_output_parts)
    def my_combine(dispatcher, parts):
      return dispatcher.combine(
          convert_gradient_to_tensor(tf.concat(parts, 0)),
          multiply_by_gates=multiply_by_gates)
    return self._dp(my_combine, self._dispatchers, expert_output_parts_t)

  def expert_to_gates(self):
    """Gate values corresponding to the examples in the per-expert `Tensor`s.

    Returns:
      a list of `num_experts` one-dimensional `Tensor`s of type `tf.float32`.
    """
    return self._ep(
        tf.concat,
        transpose_list_of_lists(
            self._dp(lambda d: d.expert_to_gates(), self._dispatchers)), 0)


def transpose_list_of_lists(lol):
  """Transpose a list of equally-sized python lists.

  Args:
    lol: a list of lists
  Returns:
    a list of lists
  """
  assert lol, "cannot pass the empty list"
  return [list(x) for x in zip(*lol)]


def ffn_expert_fn(input_size,
                  hidden_sizes,
                  output_size,
                  hidden_activation=tf.nn.relu):
  """Returns a function that creates a feed-forward network.

  Use this function to create the expert_fn argument to distributed_moe.

  Args:
    input_size: an integer
    hidden_sizes: a list of integers
    output_size: an integer
    hidden_activation: a unary function.

  Returns:
    a unary function
  """
  def my_fn(x):
    layer_sizes = [input_size] + hidden_sizes + [output_size]
    for i in xrange(1 + len(hidden_sizes)):
      w = tf.get_variable("w_%d" % i, layer_sizes[i:i+2], tf.float32)
      x = tf.matmul(x, w)
      if i < len(hidden_sizes):
        x = hidden_activation(x)
      if layer_sizes[i] != input_size:
        x *= (layer_sizes[i] / float(input_size))**-0.5
    return x
  return my_fn


def reshape_like(a, b):
  """Reshapes a to match the shape of b in all but the last dimension."""
  ret = tf.reshape(a, tf.concat([tf.shape(b)[:-1], tf.shape(a)[-1:]], 0))
  ret.set_shape(b.get_shape().as_list()[:-1] + a.get_shape().as_list()[-1:])
  return ret


def flatten_all_but_last(a):
  """Flatten all dimensions of a except the last."""
  ret = tf.reshape(a, [-1, tf.shape(a)[-1]])
  ret.set_shape([None] + a.get_shape().as_list()[-1:])
  return ret


def distributed_moe(data_parallelism,
                    expert_devices,
                    xs,
                    train,
                    input_size,
                    expert_fn,
                    num_experts,
                    k=2,
                    loss_coef=1e-2,
                    name=None):
  """Call a distributed mixture of experts.

  Args:
    data_parallelism: a expert_utils.Parallelism object.
    expert_devices: a list of strings.  We round-robin the experts across these
      devices.
    xs: a list of input tensors, each with shape [... , input_size]
    train: a boolean scalar.
    input_size: an integer (input size for this layer)
    expert_fn: a unary function for each expert to run
       It should take a Tensor with shape [batch_size, input_size]
       and return a Tensor with shape [batch_size, output_size].
       e.g. ffn_expert_fn(...)
    num_experts: an integer - number of experts
    k: an integer - how many experts to use for each batch element
    loss_coef: a scalar - multiplier on load-balancing losses
    name: a string

  Returns:
    ys: a list of tensors.  Each Tensor has the same shape as the corresponding
      Tensor in xs, except for the last dimension, which is output_size.
    extra_training_loss: a scalar.  This should be added into the overall
      training loss of the model.  The backpropagation of this loss
      encourages all experts to be approximately equally used across a batch.
  """
  dp = data_parallelism
  # create a parallelism object for running the experts.
  #   We use the default of reuse=False.  Otherwise, the experts would all
  #   use the same variables.
  ep = Parallelism(
      [expert_devices[i % len(expert_devices)] for i in xrange(num_experts)])
  # Experts expect 2d input tensors, so flatten the batch dimension and all
  # spatial dimensions together.
  xs_flat = dp(tf.reshape, xs, [[-1, input_size]] * dp.n)
  with tf.variable_scope(name, default_name="moe"):
    # The gates indicate which batch elements go to which tensors.
    # load is a measure of approximately how many examples go to each expert
    gates, load = dp(noisy_top_k_gating,
                     xs_flat,
                     num_experts,
                     train,
                     k,
                     initializer=tf.zeros_initializer(),
                     noisy_gating=True,
                     noise_epsilon=1e-2)
    # This magic object helps us shuffle data between datashards and experts.
    dispatcher = DistributedSparseDispatcher(dp, ep, gates)
    expert_in = dispatcher.dispatch(xs_flat)
    expert_out = ep(expert_fn, expert_in)
    ys_flat = dispatcher.combine(expert_out)
    ys = dp(reshape_like, ys_flat, xs)
    # compute some load-balancing losses.
    load = tf.add_n(load)
    importance = tf.add_n(dp(tf.reduce_sum, gates, 0))
    loss = loss_coef * (cv_squared(importance) + cv_squared(load))
    return ys, loss


def local_moe(x,
              train,
              expert_fn,
              num_experts,
              k=2,
              loss_coef=1e-2,
              pass_x=True,
              pass_gates=False,
              additional_dispatch_params=None,
              pad_remover=None,
              name=None):
  """Call a local mixture of experts.

  Args:
    x: a tensors with shape [... , input_size]
    train: a boolean scalar.
    expert_fn: a function.
    num_experts: an integer - number of experts
    k: an integer - how many experts to use for each batch element
    loss_coef: a scalar - multiplier on load-balancing losses
    pass_x: a boolean. If true, x will also be dispatched to the experts.
    pass_gates: a boolean. If true, gates will be passed to experts. Might be
      necessary when dealing with sparse encoder-encoder decoder attention
    additional_dispatch_params: The extra tensors that need to be sent to each
      expert. Examples include batch batch coordinates (see
      common_attention.local_expert_attention)
    pad_remover (PadRemover): If given, the padding is removed/restored before
      sending to the experts
    name: a string

  Returns:
    y: a tensor.  Has the same shape as x, except for the last dimension,
      which is output_size.
    extra_training_loss: a scalar.  This should be added into the overall
      training loss of the model.  The backpropagation of this loss
      encourages all experts to be approximately equally used across a batch.
  """

  with tf.variable_scope(name, default_name="local_moe"):
    x_flat = flatten_all_but_last(x)

    # Remove the padding tokens
    if pad_remover:
      x_flat = pad_remover.remove(x_flat)
      tf.summary.scalar(  # Should match the targets_nonpadding_tokens
          "nonpadding_tokens",
          tf.shape(x_flat)[0],
          family="experts_stats")

    # The gates indicate which batch elements go to which tensors.
    # load is a measure of approximately how many examples go to each expert
    gates, load = noisy_top_k_gating(
        x_flat,
        num_experts,
        train,
        k,
        initializer=tf.zeros_initializer(),
        noisy_gating=True,
        noise_epsilon=1e-2)
    # This magic object helps us shuffle data between datashards and experts.
    dispatcher = SparseDispatcher(num_experts, gates)

    # Set up expert_fn arguments
    expert_kwargs = {}
    if pass_x:
      expert_kwargs["x"] = dispatcher.dispatch(x_flat)
    if pass_gates:
      expert_kwargs["gates"] = dispatcher.expert_to_gates()
    for k, v in six.iteritems(additional_dispatch_params or {}):
      v = flatten_all_but_last(v)
      if pad_remover:
        v = pad_remover.remove(v)
      expert_kwargs[k] = dispatcher.dispatch(v)

    ep = Parallelism([DEFAULT_DEV_STRING] * num_experts)
    expert_outputs = ep(expert_fn, **expert_kwargs)

    y_flat = dispatcher.combine(expert_outputs)
    if pad_remover:
      y_flat = pad_remover.restore(y_flat)
    y = reshape_like(y_flat, x)

    importance = tf.reduce_sum(gates, 0)
    loss = loss_coef * (cv_squared(importance) + cv_squared(load))
    return y, loss
