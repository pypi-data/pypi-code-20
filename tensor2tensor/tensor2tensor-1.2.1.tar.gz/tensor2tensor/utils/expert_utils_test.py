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

"""Tests for tensor2tensor.utils.expert_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
from tensor2tensor.layers import common_attention
from tensor2tensor.utils import expert_utils
import tensorflow as tf


class ExpertUtilsTest(tf.test.TestCase):

  def _verify_value(self, sess, tensor, expected):
    output = sess.run(tensor)
    self.assertAllClose(output, expected, 1e-9)

  def testPadRemover(self):
    """Check that the padding remover is working correctly."""
    x_1 = tf.constant([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0, 0, 0],  # pad
        [0, 0, 0],  # pad
        [0, 0, 0],  # pad
        [10, 11, 12],
        [13, 14, 15],
        [0, 0, 0],  # pad
    ], dtype=tf.float32)
    # Get padding mask
    x_pad_mask = common_attention.embedding_to_padding(x_1)
    x_2 = tf.constant([
        [1],
        [2],
        [3],
        [4],  # pad
        [5],  # pad
        [6],  # pad
        [7],
        [8],
        [9],  # pad
    ], dtype=tf.float32)
    x_3 = tf.constant([
        1,
        2,
        3,
        4,  # pad
        5,  # pad
        6,  # pad
        7,
        8,
        9,  # pad
    ], dtype=tf.float32)

    pad_remover = expert_utils.PadRemover(x_pad_mask)

    y_1 = pad_remover.remove(x_1)
    y_2 = pad_remover.remove(x_2)
    y_3 = pad_remover.remove(x_3)

    z_1 = pad_remover.restore(y_1 * 2)
    z_2 = pad_remover.restore(y_2 * 2)
    z_3 = pad_remover.restore(y_3 * 2)

    with self.test_session() as sess:
      # Padding should have been removed
      self._verify_value(sess, y_1, [
          [1., 2., 3.],
          [4., 5., 6.],
          [7., 8., 9.],
          [10., 11., 12.],
          [13., 14., 15.],
      ])
      self._verify_value(sess, y_2, [
          [1.],
          [2.],
          [3.],
          [7.],
          [8.],
      ])
      self._verify_value(sess, y_3, [
          1.,
          2.,
          3.,
          7.,
          8.,
      ])

      # Padding should have been restored
      self._verify_value(sess, z_1, [
          [2., 4., 6.],
          [8., 10., 12.],
          [14., 16, 18.],
          [0., 0., 0.],
          [0., 0., 0.],
          [0., 0., 0.],
          [20., 22., 24.],
          [26., 28., 30.],
          [0., 0., 0.],
      ])
      self._verify_value(sess, z_2, [
          [2.],
          [4.],
          [6.],
          [0.],  # pad
          [0.],  # pad
          [0.],  # pad
          [14.],
          [16.],
          [0.],  # pad
      ])
      self._verify_value(sess, z_3, [
          2.,
          4.,
          6.,
          0.,  # pad
          0.,  # pad
          0.,  # pad
          14.,
          16.,
          0.,  # pad
      ])


if __name__ == '__main__':
  tf.test.main()
