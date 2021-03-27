# an example of using the GEOMAG_08 subroutine in geopack.f (from irbem).
# first, a fortran subroutine that takes arrays is used to wrap GEOMAG_08.
# then it is passed to jitFORTRAN.
import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
import jitFORTRAN
import cxtransform as cx
from datetime import datetime 
from matplotlib import pyplot as plt

# Tsyganenko uses Geocentric-Solar Wind GSW instead of GSM. GSW has the positive
# x-axis pointing antiparallel to the solar wind. He chose this coordinate system
# in order to simplify his code. GSW becomes identical to GSM when the solar Wind
# velocity travels only in the negative x-axis direction, Tsyganenko chose
#  <-400,0,0> SMGSW_08
debug = True

# allowable timeframe 1965-2020
IYEAR = 1997
IDAY = 1
IHOUR = 0
MIN = 0
ISEC = 0

# controls the direction of tranformation
# if J>0, then X1,Y1,Z1 -> X2, Y2,Z2
# if J<0, then X1,Y1,Z1 <- X2, Y2,Z2
J = 1

X1 = np.arange(0,10,dtype=np.float64)
Y1 = np.arange(0,10,dtype=np.float64)
Z1 = np.arange(0,10,dtype=np.float64)
X2 = np.arange(0,10,dtype=np.float64)
Y2 = np.arange(0,10,dtype=np.float64)
Z2 = np.arange(0,10,dtype=np.float64)

N = X1.size

wrapper_subroutine_name='SMGSW_08_V'
with open(wrapper_subroutine_name+'.txt','r') as f:
    wrapper_script = ''.join(f.readlines())

# geomag_08_V_F = jitFORTRAN.Fortran_Subroutine(wrapper_script,
#                                               wrapper_subroutine_name,
#                                               include='geopack_08')
#
# geomag_08_V_F.execute(X1,Y1,Z1,X2,Y2,Z2,
#                     J,
#                     IYEAR,IDAY,IHOUR,MIN,ISEC,
#                     N)
time = "{0:04d} {1:03d} {2:02d} {3:02d} {4:02d}".format(IYEAR, IDAY, IHOUR, MIN, ISEC)
time = datetime.strptime(time, "%Y %j %H %M %S")
time = [time.year,time.month, time.day, time.hour,time.minute,time.second]
if J>0:
    points = np.column_stack((X1,Y1,Z1))
    gp_points = np.column_stack((X2,Y2,Z2))
    if wrapper_subroutine_name=='SMGSW_08_V':
        sc_points = cx.SMtoGSM(points,time,'car','car')
    

    

if debug:
    print(X1)
    print(Y1)
    print(Z1)
    print(X2)
    print(Y2)
    print(Z2)
