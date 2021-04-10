import numpy as np
import cxtransform as cx  ## replace with pure spacepy call 
from datetime import datetime
import time


# options: SMGSW_08_V , GEOMAG_08_V
wrapper_subroutine_name='GEOMAG_08_V'
# allowable timeframe 1965-2020
IYEAR = 1997
IDAY = 1
IHOUR = 0
MIN = 0
ISEC = 0


J = 1 # test out 1 and -1 for both sc and gp
arr_size = 10**7
X1 = np.ones(arr_size,dtype=np.float64)
Y1 = np.ones(arr_size,dtype=np.float64)
Z1 = np.ones(arr_size,dtype=np.float64)
X2 = np.zeros(arr_size, dtype=np.float64)
Y2 = np.zeros(arr_size, dtype=np.float64)
Z2 = np.zeros(arr_size, dtype=np.float64)

N = X1.size


time1 = "{0:04} {1:03d} {2:02d} {3:02d} {4:02d}".format(IYEAR, IDAY, IHOUR, MIN, ISEC)
time1 = datetime.strptime(time1, "%Y %j %H %M %S")
time1 = [time1.year,time1.month, time1.day, time1.hour,time1.minute,time1.second]


points = np.column_stack((X1,Y1,Z1))
gp_points = np.column_stack((X2,Y2,Z2))
start_time = time.time()
if wrapper_subroutine_name=='SMGSW_08_V':
    sc_points = cx.SMtoGSM(points,time1,'car','car')
    title='SM to GSW'
elif wrapper_subroutine_name=='GEOMAG_08_V':
    sc_points = cx.GEOtoMAG(points,time1,'car','car')
    title='GEO to MAG'
print("--- %s seconds ---" % (time.time() - start_time))
