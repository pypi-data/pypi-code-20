# This file is generated by /tmp/pip-xdv_i9bw-build/-c
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

atlas_3_10_info={}
lapack_mkl_info={}
lapack_opt_info={'include_dirs': ['/usr/include'], 'define_macros': [('ATLAS_INFO', '"\\"3.8.3\\""')], 'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib/atlas-sse2'], 'language': 'c'}
openblas_lapack_info={}
atlas_threads_info={'include_dirs': ['/usr/include'], 'define_macros': [('ATLAS_INFO', '"\\"3.8.3\\""')], 'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib/atlas-sse2'], 'language': 'c'}
atlas_3_10_threads_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    