from fortran_code import geopy
from vtk_export import vtk_export
import numpy as np
"""
next steps
1. run one line and create a vtk
2. choose 4 footpoints on the earths surface using spherical coordinates
    and then use a coordinate transformation to switch between spherical and
    rectangular coordinates
        >> should I just create a wrapper for geopy carsph_08 or find one online?
3. create all the same graphs/vtk files.
"""
# run recalc to set data blocks
year = 2000
day = 1
hr = 0
minute = 0
sec = 0
date = np.array([year,day,hr,minute,sec])

arr_size = 10
X1 = np.arange(0,arr_size,dtype=np.float64)
Y1 = np.arange(0,arr_size,dtype=np.float64)
Z1 = np.arange(0,arr_size,dtype=np.float64)
Xout,Yout,Zout = geopy.gptransform(X1,Y1,Z1,'SMtoGSM',date)

print(Xout)
print(Yout)
print(Zout)
