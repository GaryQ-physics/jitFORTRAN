#!/bin/sh
## run in terminal to execute example
## to view the source files in example, use $ cat *

gfortran -c subroutine_1.f
gfortran -c subroutine_2.f
gfortran -c main.f
gfortran main.o subroutine_1.o subroutine_2.o
./a.out
rm a.out
rm *.o

python jit_subroutine_1.py
python jit_subroutine_2.py
python jit_both.py
