import os
from ctypes import cdll, c_void_p, c_size_t, c_uint32, create_string_buffer
from zof.connection import Connection

OFTR_DLL = None


def _dll():
    global OFTR_DLL  # pylint: disable=global-statement
    if OFTR_DLL is not None:
        return OFTR_DLL

    executable = Connection.find_oftr_path(os.getenv('ZOF_OFTR_PATH'))
    if not executable or executable[0] != '/':
        raise RuntimeError('Unable to locate oftr executable')

    OFTR_DLL = cdll.LoadLibrary(executable)
    OFTR_DLL.oftr_call.argtypes = [
        c_uint32, c_void_p, c_size_t, c_void_p, c_size_t
    ]
    return OFTR_DLL


def _oftr_call(opcode, data, buflen=2048):
    dll = _dll()
    buf = create_string_buffer(buflen)

    result = dll.oftr_call(opcode, data, len(data), buf, buflen)
    if result < -buflen:
        # Result buffer is not big enough.
        buflen = -result
        buf = create_string_buffer(buflen)
        result = dll.oftr_call(opcode, data, len(data), buf, buflen)

    if result >= 0:
        return buf[:result]
    if result >= -buflen:
        raise ValueError('error: %s' % buf[:-result])
    raise ValueError('error: _oftr_call failed: %r' % result)


def encode(text, version=4):
    """Encode source code as binary.
    """

    opcode = 1 + (version << 24)
    return _oftr_call(opcode, text.encode('utf-8'), buflen=max(len(text), 1024))
