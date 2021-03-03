gfortran -c sub.f
gfortran main.f sub.o

#since it's statically linked (?), can remove .o before running executable
rm sub.o

./a.out

rm a.out
