from .PyrexTypes import BufferType, CType, CTypedefType, CStructOrUnionType

_pythran_var_prefix = "__pythran__"
# Pythran/Numpy specific operations
def has_np_pythran(env):
    while not env is None:
        if hasattr(env, "directives") and env.directives.get('np_pythran', False):
            return True
        env = env.outer_scope

def is_pythran_supported_dtype(type_):
    if isinstance(type_, CTypedefType):
        return is_pythran_supported_type(type_.typedef_base_type)
    return type_.is_numeric

def pythran_type(Ty,ptype="ndarray"):
    if Ty.is_buffer:
        ndim,dtype = Ty.ndim, Ty.dtype
        if isinstance(dtype, CStructOrUnionType):
            ctype = dtype.cname
        elif isinstance(dtype, CType):
            ctype = dtype.sign_and_name()
        elif isinstance(dtype, CTypedefType):
            ctype = dtype.typedef_cname
        else:
            raise ValueError("unsupported type %s!" % str(dtype))
        return "pythonic::types::%s<%s,%d>" % (ptype,ctype, ndim)
    from .PyrexTypes import PythranExpr
    if Ty.is_pythran_expr:
        return Ty.pythran_type
    #if Ty.is_none:
    #    return "decltype(pythonic::__builtin__::None)"
    if Ty.is_numeric:
        return Ty.sign_and_name()
    raise ValueError("unsupported pythran type %s (%s)" % (str(Ty), str(type(Ty))))
    return None

def type_remove_ref(ty):
    return "typename std::remove_reference<%s>::type" % ty

def pythran_binop_type(op, tA, tB):
    return "decltype(std::declval<%s>() %s std::declval<%s>())" % \
        (pythran_type(tA), op, pythran_type(tB))

def pythran_unaryop_type(op, type_):
    return "decltype(%sstd::declval<%s>())" % (
        op, pythran_type(type_))

def pythran_indexing_type(type_, indices):
    def index_code(idx):
        if idx.is_slice:
            if idx.step.is_none:
                func = "contiguous_slice"
                n = 2
            else:
                func = "slice"
                n = 3
            return "pythonic::types::%s(%s)" % (func,",".join(["0"]*n))
        elif idx.type.is_int:
            return "std::declval<long>()"
        elif idx.type.is_pythran_expr:
            return "std::declval<%s>()" % idx.type.pythran_type
        raise ValueError("unsupported indice type %s!" % idx.type)
    indexing = ",".join(index_code(idx) for idx in indices)
    return type_remove_ref("decltype(std::declval<%s>()(%s))" % (pythran_type(type_), indexing))

def pythran_indexing_code(indices):
    def index_code(idx):
        if idx.is_slice:
            values = idx.start, idx.stop, idx.step
            if idx.step.is_none:
                func = "contiguous_slice"
                values = values[:2]
            else:
                func = "slice"
            return "pythonic::types::%s(%s)" % (func,",".join((v.pythran_result() for v in values)))
        elif idx.type.is_int:
            return idx.result()
        elif idx.type.is_pythran_expr:
            return idx.pythran_result()
        raise ValueError("unsupported indice type %s!" % str(idx.type))
    return ",".join(index_code(idx) for idx in indices)

def pythran_func_type(func, args):
    args = ",".join(("std::declval<%s>()" % pythran_type(a.type) for a in args))
    return "decltype(pythonic::numpy::functor::%s{}(%s))" % (func, args)

def to_pythran(op,ptype=None):
    op_type = op.type
    if is_type(op_type,["is_pythran_expr", "is_int", "is_numeric", "is_float",
        "is_complex"]):
        return op.result()
    if op.is_none:
        return "pythonic::__builtin__::None"
    if ptype is None:
        ptype = pythran_type(op_type)
    assert(op.type.is_pyobject)
    return "from_python<%s>(%s)" % (ptype, op.py_result())

def from_pythran():
    return "to_python"

def is_type(type_, types):
    for attr in types:
        if getattr(type_, attr, False):
            return True
    return False

def is_pythran_supported_node_or_none(node):
    return node.is_none or is_pythran_supported_type(node.type)

def is_pythran_supported_type(type_):
    pythran_supported = (
        "is_pythran_expr", "is_int", "is_numeric", "is_float", "is_none",
        "is_complex")
    return is_type(type_, pythran_supported) or is_pythran_expr(type_)

def is_pythran_supported_operation_type(type_):
    pythran_supported = (
        "is_pythran_expr", "is_int", "is_numeric", "is_float", "is_complex")
    return is_type(type_,pythran_supported) or is_pythran_expr(type_)

def is_pythran_expr(type_):
    return type_.is_pythran_expr

def is_pythran_buffer(type_):
    return type_.is_numpy_buffer and is_pythran_supported_dtype(type_.dtype) and \
           type_.mode in ("c","strided") and not type_.cast

def include_pythran_generic(env):
    # Generic files
    env.add_include_file("pythonic/core.hpp")
    env.add_include_file("pythonic/python/core.hpp")
    env.add_include_file("pythonic/types/bool.hpp")
    env.add_include_file("pythonic/types/ndarray.hpp")
    env.add_include_file("<new>") # for placement new

    for i in (8,16,32,64):
        env.add_include_file("pythonic/types/uint%d.hpp" % i)
        env.add_include_file("pythonic/types/int%d.hpp" % i)
    for t in ("float", "float32", "float64", "set", "slice", "tuple", "int",
            "long", "complex", "complex64", "complex128"):
        env.add_include_file("pythonic/types/%s.hpp" % t)

def include_pythran_type(env, type_):
    pass

def type_is_numpy(type_):
    if not hasattr(type_, "is_numpy"):
        return False
    return type_.is_numpy
