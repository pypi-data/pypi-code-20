import numpy
from mpi4py import MPI
import warnings
import functools

def split_size_3d(s):
    """
    Split `s` into three integers, a, b, c, such
    that a * b * c == s and a <= b <= c

    Parameters
    -----------
    s : int
        integer to split

    Returns
    -------
    a, b, c: int
        integers such that a * b * c == s and a <= b <= c
    """
    a = int(s** 0.3333333) + 1
    d = s
    while a > 1:
        if s % a == 0:
            s = s // a
            break
        a = a - 1
    b = int(s ** 0.5) + 1
    while b > 1:
        if s % b == 0:
            s = s // b
            break
        b = b - 1
    c = s
    return a, b, c

def deprecate(name, alternative, alt_name=None):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used.
    """
    alt_name = alt_name or alternative.__name__

    def wrapper(*args, **kwargs):
        warnings.warn("%s is deprecated. Use %s instead" % (name, alt_name),
                      FutureWarning, stacklevel=2)
        return alternative(*args, **kwargs)
    return wrapper

def GatherArray(data, comm, root=0):
    """
    Gather the input data array from all ranks to the specified ``root``.

    This uses `Gatherv`, which avoids mpi4py pickling, and also
    avoids the 2 GB mpi4py limit for bytes using a custom datatype

    Parameters
    ----------
    data : array_like
        the data on each rank to gather
    comm : MPI communicator
        the MPI communicator
    root : int
        the rank number to gather the data to

    Returns
    -------
    recvbuffer : array_like, None
        the gathered data on root, and `None` otherwise
    """
    if not isinstance(data, numpy.ndarray):
        raise ValueError("`data` must by numpy array in GatherArray")

    # need C-contiguous order
    if not data.flags['C_CONTIGUOUS']:
        data = numpy.ascontiguousarray(data)
    local_length = data.shape[0]

    # check dtypes and shapes
    shapes = comm.gather(data.shape, root=root)
    dtypes = comm.allgather(data.dtype)

    # check for structured data
    if dtypes[0].char == 'V':

        # check for structured data mismatch
        names = set(dtypes[0].names)
        if any(set(dt.names) != names for dt in dtypes[1:]):
            raise ValueError("mismatch between data type fields in structured data")

        # check for 'O' data types
        if any(dtypes[0][name] == 'O' for name in dtypes[0].names):
            raise ValueError("object data types ('O') not allowed in structured data in GatherArray")

        # compute the new shape for each rank
        newlength = comm.allreduce(local_length)
        newshape = list(data.shape)
        newshape[0] = newlength

        # the return array
        if comm.rank == root:
            recvbuffer = numpy.empty(newshape, dtype=dtypes[0], order='C')
        else:
            recvbuffer = None

        for name in dtypes[0].names:
            d = GatherArray(data[name], comm, root=root)
            if comm.rank == 0:
                recvbuffer[name] = d

        return recvbuffer

    # check for 'O' data types
    if dtypes[0] == 'O':
        raise ValueError("object data types ('O') not allowed in structured data in GatherArray")

    # check for bad dtypes and bad shapes
    if comm.rank == root:
        bad_shape = any(s[1:] != shapes[0][1:] for s in shapes[1:])
        bad_dtype = any(dt != dtypes[0] for dt in dtypes[1:])
    else:
        bad_shape = None; bad_dtype = None

    bad_shape, bad_dtype = comm.bcast((bad_shape, bad_dtype))
    if bad_shape:
        raise ValueError("mismatch between shape[1:] across ranks in GatherArray")
    if bad_dtype:
        raise ValueError("mismatch between dtypes across ranks in GatherArray")

    shape = data.shape
    dtype = data.dtype

    # setup the custom dtype
    duplicity = numpy.product(numpy.array(shape[1:], 'intp'))
    itemsize = duplicity * dtype.itemsize
    dt = MPI.BYTE.Create_contiguous(itemsize)
    dt.Commit()

    # compute the new shape for each rank
    newlength = comm.allreduce(local_length)
    newshape = list(shape)
    newshape[0] = newlength

    # the return array
    if comm.rank == root:
        recvbuffer = numpy.empty(newshape, dtype=dtype, order='C')
    else:
        recvbuffer = None

    # the recv counts
    counts = comm.allgather(local_length)
    counts = numpy.array(counts, order='C')

    # the recv offsets
    offsets = numpy.zeros_like(counts, order='C')
    offsets[1:] = counts.cumsum()[:-1]

    # gather to root
    comm.Barrier()
    comm.Gatherv([data, dt], [recvbuffer, (counts, offsets), dt], root=root)
    dt.Free()

    return recvbuffer

def ScatterArray(data, comm, root=0, counts=None):
    """
    Scatter the input data array across all ranks, assuming `data` is
    initially only on `root` (and `None` on other ranks).

    This uses ``Scatterv``, which avoids mpi4py pickling, and also
    avoids the 2 GB mpi4py limit for bytes using a custom datatype

    Parameters
    ----------
    data : array_like or None
        on `root`, this gives the data to split and scatter
    comm : MPI communicator
        the MPI communicator
    root : int
        the rank number that initially has the data
    counts : list of int
        list of the lengths of data to send to each rank

    Returns
    -------
    recvbuffer : array_like
        the chunk of `data` that each rank gets
    """
    import logging

    if counts is not None:
        counts = numpy.asarray(counts, order='C')
        if len(counts) != comm.size:
            raise ValueError("counts array has wrong length!")

    # check for bad input
    if comm.rank == root:
        bad_input = not isinstance(data, numpy.ndarray)
    else:
        bad_input = None
    bad_input = comm.bcast(bad_input)
    if bad_input:
        raise ValueError("`data` must by numpy array on root in ScatterArray")

    if comm.rank == 0:
        # need C-contiguous order
        if not data.flags['C_CONTIGUOUS']:
            data = numpy.ascontiguousarray(data)
        shape_and_dtype = (data.shape, data.dtype)
    else:
        shape_and_dtype = None

    # each rank needs shape/dtype of input data
    shape, dtype = comm.bcast(shape_and_dtype)

    # object dtype is not supported
    fail = False
    if dtype.char == 'V':
         fail = any(dtype[name] == 'O' for name in dtype.names)
    else:
        fail = dtype == 'O'
    if fail:
        raise ValueError("'object' data type not supported in ScatterArray; please specify specific data type")

    # initialize empty data on non-root ranks
    if comm.rank != root:
        np_dtype = numpy.dtype((dtype, shape[1:]))
        data = numpy.empty(0, dtype=np_dtype)

    # setup the custom dtype
    duplicity = numpy.product(numpy.array(shape[1:], 'intp'))
    itemsize = duplicity * dtype.itemsize
    dt = MPI.BYTE.Create_contiguous(itemsize)
    dt.Commit()

    # compute the new shape for each rank
    newshape = list(shape)

    if counts is None:
        newlength = shape[0] // comm.size
        if comm.rank < shape[0] % comm.size:
            newlength += 1
        newshape[0] = newlength
    else:
        if counts.sum() != shape[0]:
            raise ValueError("the sum of the `counts` array needs to be equal to data length")
        newshape[0] = counts[comm.rank]

    # the return array
    recvbuffer = numpy.empty(newshape, dtype=dtype, order='C')

    # the send counts, if not provided
    if counts is None:
        counts = comm.allgather(newlength)
        counts = numpy.array(counts, order='C')

    # the send offsets
    offsets = numpy.zeros_like(counts, order='C')
    offsets[1:] = counts.cumsum()[:-1]

    # do the scatter
    comm.Barrier()
    comm.Scatterv([data, (counts, offsets), dt], [recvbuffer, dt])
    dt.Free()
    return recvbuffer


def attrs_to_dict(obj, prefix):
    if not hasattr(obj, 'attrs'):
        return {}

    d = {}
    for key, value in obj.attrs.items():
        d[prefix + key] = value
    return d

import json
from astropy.units import Quantity, Unit
from nbodykit.cosmology import Cosmology

class JSONEncoder(json.JSONEncoder):
    """
    A subclass of :class:`json.JSONEncoder` that can also handle numpy arrays,
    complex values, and :class:`astropy.units.Quantity` objects.
    """
    def default(self, obj):

        # Cosmology object
        if isinstance(obj, Cosmology):
            d = {}
            d['__cosmo__'] = True
            d['__args__'] = obj.args.copy()
            d['__args__'].update(obj.kwargs)
            return d

        # astropy quantity
        if isinstance(obj, Quantity):

            d = {}
            d['__unit__'] = str(obj.unit)

            value = obj.value
            if obj.size > 1:
                d['__dtype__'] = value.dtype.str if value.dtype.names is None else value.dtype.descr
                d['__shape__'] = value.shape
                value = value.tolist()

            d['__data__'] = value
            return d

        # complex values
        elif isinstance(obj, complex):
            return {'__complex__': [obj.real, obj.imag ]}

        # numpy arrays
        elif isinstance(obj, numpy.ndarray):
            value = obj
            dtype = obj.dtype
            d = {
                '__dtype__' :
                    dtype.str if dtype.names is None else dtype.descr,
                '__shape__' : value.shape,
                '__data__': value.tolist(),
            }
            return d
        # explicity convert numpy data types to python types
        # see: https://bugs.python.org/issue24313
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.integer):
            return int(obj)

        return json.JSONEncoder.default(self, obj)

class JSONDecoder(json.JSONDecoder):
    """
    A subclass of :class:`json.JSONDecoder` that can also handle numpy arrays,
    complex values, and :class:`astropy.units.Quantity` objects.
    """
    @staticmethod
    def hook(value):
        def fixdtype(dtype):
            if isinstance(dtype, list):
                true_dtype = []
                for field in dtype:
                    if len(field) == 3:
                        true_dtype.append((str(field[0]), str(field[1]), field[2]))
                    if len(field) == 2:
                        true_dtype.append((str(field[0]), str(field[1])))
                return true_dtype
            return dtype

        def fixdata(data, N, dtype):
            if not isinstance(dtype, list):
                return data

            # for structured array,
            # the last dimension shall be a tuple
            if N > 0:
                return [fixdata(i, N - 1, dtype) for i in data]
            else:
                assert len(data) == len(dtype)
                return tuple(data)

        d = None
        if '__dtype__' in value:
            dtype = fixdtype(value['__dtype__'])
            shape = value['__shape__']
            a = fixdata(value['__data__'], len(shape), dtype)
            d = numpy.array(a, dtype=dtype)

        if '__unit__' in value:
            if d is None:
                d = value['__data__']
            d = Quantity(d, Unit(value['__unit__']))

        if '__cosmo__' in value:
            d = Cosmology(**value['__args__'])

        if d is not None:
            return d

        if '__complex__' in value:
            real, imag = value['__complex__']
            return real + 1j * imag

        return value

    def __init__(self, *args, **kwargs):
        kwargs['object_hook'] = JSONDecoder.hook
        json.JSONDecoder.__init__(self, *args, **kwargs)

def timer(start, end):
    """
    Utility function to return a string representing the elapsed time,
    as computed from the input start and end times

    Parameters
    ----------
    start : int
        the start time in seconds
    end : int
        the end time in seconds

    Returns
    -------
    str :
        the elapsed time as a string, using the format `hours:minutes:seconds`
    """
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)
