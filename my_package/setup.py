from setuptools import setup, find_packages, Extension
# from numpy.distutils.fcompiler import get_default_fcompiler

# # Determine the Fortran compiler
# fcompiler = get_default_fcompiler()

# # Define the Fortran extension module
# hello_fortran_module = Extension('_hello_fortran',
#                                 sources=['my_package/hello.f90'],
#                                 extra_f90_compile_args=['-fPIC'],
#                                 f2py_options=['--quiet'],
#                                 f2py_fcompiler=fcompiler)

# hello_cpp_module = Extension('_hello_cpp',
#                             sources=['my_package/hello.cpp'],
#                             extra_compile_args=['-std=c++11', '-fPIC'])

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    # ext_modules=[hello_cpp_module, hello_fortran_module],
    entry_points={
        'console_scripts': [
            'print-cctbx-version=my_package:print_cctbx_version',
        ],
    },
)
