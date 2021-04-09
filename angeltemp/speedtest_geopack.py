import jitFORTRAN_exe as jit
import numpy as np
import time

iyear = 1990
iday = 1
ihour = 0
min_bn = 0
isec = 0

arr_size = 10**8
X1 = np.ones(arr_size,dtype=np.float64)
Y1 = np.ones(arr_size,dtype=np.float64)
Z1 = np.ones(arr_size,dtype=np.float64)

X2 = np.zeros(arr_size, dtype=np.float64)
Y2 = np.zeros(arr_size, dtype=np.float64)
Z2 = np.zeros(arr_size, dtype=np.float64)

n = X1.size
start_time = time.time()
jit.geomag_08_v(X1,Y1,Z1,X2,Y2,Z2,
            1,
            iyear,iday,ihour,min_bn,isec,n)
print("--- %s seconds ---" % (time.time() - start_time))
