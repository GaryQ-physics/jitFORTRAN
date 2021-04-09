import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
import jitFORTRAN
import time



debug = False

# options: SMGSW_08_V , GEOMAG_08_V
wrapper_subroutine_name='GEOMAG_08_V'
# allowable timeframe 1965-2020
IYEAR = 1997
IDAY = 1
IHOUR = 0
MIN = 0
ISEC = 0

J = 1 # test out 1 and -1 for both sc and gp
arr_size = 10**3
X1 = np.arange(0,arr_size,dtype=np.float64)
Y1 = np.arange(0,arr_size,dtype=np.float64)
Z1 = np.arange(0,arr_size,dtype=np.float64)

X2 = np.zeros(arr_size, dtype=np.float64)
Y2 = np.zeros(arr_size, dtype=np.float64)
Z2 = np.zeros(arr_size, dtype=np.float64)

N = X1.size

with open(wrapper_subroutine_name+'.txt','r') as f:
    wrapper_script = ''.join(f.readlines())

geomag_08_V_F = jitFORTRAN.Fortran_Subroutine(wrapper_script,
                                              wrapper_subroutine_name,
                                              include='geopack_08')



### two ways either do .execute once with a small array to compile
### or call .compile() before the .execute()

start_time = time.time()
geomag_08_V_F.execute(X1,Y1,Z1,X2,Y2,Z2,
                    J,
                    IYEAR,IDAY,IHOUR,MIN,ISEC,
                    N)

print("--- %s seconds ---" % (time.time() - start_time))
