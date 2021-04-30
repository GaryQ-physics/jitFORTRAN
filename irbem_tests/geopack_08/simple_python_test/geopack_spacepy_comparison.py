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
import time as tm

# Tsyganenko uses Geocentric-Solar Wind GSW instead of GSM. GSW has the positive
# x-axis pointing antiparallel to the solar wind. He chose this coordinate system
# in order to simplify his code. GSW becomes identical to GSM when the solar Wind
# velocity travels only in the negative x-axis direction, Tsyganenko chose
#  <-400,0,0> SMGSW_08
debug = False

# options: SMGSW_08_V , GEOMAG_08_V, 
# to be made: SPHCAR_08_V, 
#   GEODGEO_08_V ** this one will be strange


# controls the direction of tranformation
# generic_tranformation(X1,Y1,Z1,X2,Y2,Z2,J)
# if J>0, then X1,Y1,Z1 -> X2, Y2,Z2
# if J<0, then X1,Y1,Z1 <- X2, Y2,Z2
trans = ['GEItoGEO','GEOtoGEI',
         'GEOtoGSM','GSMtoGSM',
         'GEOtoMAG','MAGtoGEO',
         'GSMtoGSE','GSEtoGSM',
         'MAGtoSM','SMtoMAG',
         'SMtoGSM','GSMtoSM',
         # the following rely on more than one geopack function
         ] 


# test out 1 and -1 for both sc and gp
# done but not tested: GSWGSE_08_V, GEIGEO_08_V, MAGSM_08_V, GEOGSW_08_V
# one_sec_diff = True
# wrap_sub_names = ['SMGSW_08_V','GEOMAG_08_V','GSWGSE_08_V','GEIGEO_08_V',
#                      'MAGSM_08_V','GEOGSW_08_V']
wrap_sub_name = 'gptransform'
for t in trans:
    # allowable timeframe 1965-2020
    IYEAR = 1997
    IDAY = 1
    IHOUR = 0
    MIN = 0
    ISEC = 0
    
    

    arr_size = 23**1
    X1 = np.arange(0,arr_size,dtype=np.float64)
    Y1 = np.arange(0,arr_size,dtype=np.float64)
    Z1 = np.arange(0,arr_size,dtype=np.float64)
    
    N = X1.size
    
    with open(wrap_sub_name +'.txt','r') as f:
        wrapper_script = ''.join(f.readlines())
    
    geomag_08_V_F = jitFORTRAN.Fortran_Subroutine(wrapper_script,
                                                  wrap_sub_name,
                                                  include='geopack_08')
    
    X2, Y2, Z2 = geomag_08_V_F.execute(X1,Y1,Z1,
                                       t,
                                       IYEAR,IDAY,IHOUR,MIN,ISEC
                                       )
    
    # time = "{0:04} {1:03d} {2:02d} {3:02d} {4:02d}".format(IYEAR, IDAY, IHOUR, MIN, ISEC)
    # time = datetime.strptime(time, "%Y %j %H %M %S")
    # time = [time.year,time.month, time.day, time.hour,time.minute,time.second]
    

    # if J>0:
    #     points = np.column_stack((X1,Y1,Z1))
    #     gp_points = np.column_stack((X2,Y2,Z2))

    #     if wrap_sub_name=='SMGSW_08_V':
    #         sc_points = cx.SMtoGSM(points,time,'car','car')
    #         title='SM to GSW'
    #     elif wrap_sub_name=='GEOMAG_08_V':
    #         sc_points = cx.GEOtoMAG(points,time,'car','car')
    #         title='GEO to MAG'
    #     elif wrap_sub_name=='GSWGSE_08_V':
    #         sc_points = cx.GSMtoGSE(points,time,'car','car')
    #         title='GSM to GSE'
    #     elif wrap_sub_name=='GEIGEO_08_V':
    #         sc_points = cx.GEItoGEO(points,time,'car','car')
    #         title='GEI to GEO'
    #     elif wrap_sub_name=='MAGSM_08_V':
    #         sc_points = cx.MAGtoSM(points,time,'car','car')
    #         title='MAG to SM'
    #     elif wrap_sub_name=='GEOGSW_08_V':
    #         sc_points = cx.GEOtoGSW(points,time,'car','car')
    #         title='GEO to GSW'
    # else:
    #     points = np.column_stack((X2,Y2,Z2))
    #     gp_points = np.column_stack((X1,Y1,Z1))
    #     if wrap_sub_name=='SMGSW_08_V':
    #         # print('i got hit!\n')
    #         sc_points = cx.GSMtoSM(points,time,'car','car')
    #         title='GSM to SM'
    #     elif wrap_sub_name=='GEOMAG_08_V':
    #         sc_points = cx.MAGtoGEO(points,time,'car','car')
    #         title='MAG to GEO'
        
    # plt.plot(points[:,0],sc_points[:,0] - gp_points[:,0])
    # plt.title(title + ' x-axis')
    # plt.xlabel('1 unit')
    # plt.ylabel('spacepy - geopack x-axis')
    # plt.show()
    # plt.savefig('figures/'+title + 'x_axis')
    
    # plt.plot(points[:,1],sc_points[:,1] - gp_points[:,1])
    # plt.title(title + ' y-axis')
    # plt.xlabel('1 unit')
    # plt.ylabel('spacepy - geopack y-axis')
    # plt.show()
    # plt.savefig('figures/'+title + 'y_axis')
    
    # plt.plot(points[:,2],sc_points[:,2] - gp_points[:,2])
    # plt.title(title + ' z-axis')
    # plt.xlabel('1 unit')
    # plt.ylabel('spacepy - geopack z-axis')
    # plt.show()
    # plt.savefig('figures/'+title + 'z_axis')

    # if one_sec_diff:
    #     # allowable timeframe 1965-2020

    #     ISEC += 1
        
    #     X2 = np.zeros(arr_size, dtype=np.float64)
    #     Y2 = np.zeros(arr_size, dtype=np.float64)
    #     Z2 = np.zeros(arr_size, dtype=np.float64)
        

    #     start_time = tm.time()
    #     geomag_08_V_F.execute(X1,Y1,Z1,X2,Y2,Z2,
    #                         J,
    #                         IYEAR,IDAY,IHOUR,MIN,ISEC,
    #                         N)
    #     points_1sec = np.column_stack((X2,Y2,Z2))
        
    #     print("%s --- %s seconds ---" % (title,tm.time() - start_time))
    #     print('\n\n        stop!\n\n')
    #     plt.plot(points[:,0],points_1sec[:,0] - gp_points[:,0])
    #     plt.title(title + ' x-axis, 1s difference')
    #     plt.xlabel('1 unit')
    #     plt.ylabel('geopack 1s - geopack 0s x-axis')
    #     plt.show()
    #     plt.savefig('figures/'+title + 'x_axis 1s diff')
        
        # plt.plot(points[:,1],points_1sec[:,1] - gp_points[:,1])
        # plt.title(title + ' y-axis, 1s difference')
        # plt.xlabel('1 unit')
        # plt.ylabel('geopack 1s - geopack 0s sec y-axis')
        # plt.show()
        # plt.savefig('figures/'+title + 'x_axis 1s diff')
        
        # plt.plot(points[:,0],points_1sec[:,0] - gp_points[:,0])
        # plt.title(title + ' x-axis, 1s difference')
        # plt.xlabel('1 unit')
        # plt.ylabel('geopack 1s - geopack 0s x-axis')
        # plt.show()
        # plt.savefig('figures/'+title + 'x_axis 1s diff')
