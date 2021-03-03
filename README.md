# jitFORTRAN
FORTRAN interface for python.
Using numpy's f2py, compile a python string of fortran code at runtime and run the resulting subroutines on numpy arrays.
Can also link in seperate fortran ```sourcecode.f```, if gfortran installed.

works for python2.
Not currntly implemended for python3

Works on Unix like operating systems.
Not currently implemented for Windows.
