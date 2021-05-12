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
trans = []
csys = ['GSM','SM','GSE','MAG','GEO','GEI']
for c1 in csys:
    for c2 in csys:
        if c1 != c2:
            trans.append('to'.join((c1,c2)))

fsys = open('csys_trans_analysis.txt','w')


# test out 1 and -1 for both sc and gp
# done but not tested: GSWGSE_08_V, GEIGEO_08_V, MAGSM_08_V, GEOGSW_08_V
# one_sec_diff = True
# wrap_sub_names = ['SMGSW_08_V','GEOMAG_08_V','GSWGSE_08_V','GEIGEO_08_V',
#                      'MAGSM_08_V','GEOGSW_08_V']
ev = []
wrap_sub_name = 'gptransform'
with open(wrap_sub_name +'.txt','r') as f:
        wrapper_script = ''.join(f.readlines())
geomag_08_V_F = jitFORTRAN.Fortran_Subroutine(wrapper_script,
                                                  wrap_sub_name,
                                                  include='geopack_08')
for t in trans:
    # allowable timeframe 1965-2020

    dtime = np.array((1997,1,0,0,0)) # default is np.int64 to match fortran INTEGER*8
    
    

    arr_size = 100
    X1 = np.arange(0,arr_size,dtype=np.float64)
    Y1 = np.arange(0,arr_size,dtype=np.float64)
    Z1 = np.arange(0,arr_size,dtype=np.float64)
    
    N = X1.size
    
    
    
    
    
    X2, Y2, Z2 = geomag_08_V_F.execute(X1,Y1,Z1,
                                       t,
                                       dtime
                                       )
    
    time = "{0:04} {1:03d} {2:02d} {3:02d} {4:02d}".format(dtime[0], 
                                                           dtime[1], dtime[2], 
                                                           dtime[3], dtime[4])
    time = datetime.strptime(time, "%Y %j %H %M %S")
    time = [time.year,time.month, time.day, time.hour,time.minute,time.second]
    
    initial, final = t.split('to')
    
    spcoord = cx.transform(np.column_stack([X1,Y1,Z1]), time, initial, final)
    geocoord = np.column_stack([X2,Y2,Z2])
    magdiff = np.linalg.norm(geocoord-spcoord)/np.linalg.norm(spcoord)
    ev.append(magdiff)
    fsys.write("{} : {}\n".format(t, magdiff))

fsys.close()


"""
analysis thus far leads me to believe that the problem is with 
multiple calls since they tend to have the largest  error. 
perhaps I should create an intermediate vector tempx tempy tempz. 

This is the results mag(spcoord-geocoord)/mag(geocoord)

    GSMtoSM : 0.000109721573247
    GSMtoGSE : 0.000332588127469
    GSMtoMAG : 0.361201084308       - double - uses MAGSM SMGSW
    GSMtoGEO : 0.000329302792926
    GSMtoGEI : 1.13805818542        - double - uses GEOGSW GEIGEO
    SMtoGSM : 0.000109721573247
    SMtoGSE : 0.342871033723        - double - uses SMGWE GSWGSE
    SMtoMAG : 7.15463008082e-05
    SMtoGEO : 1.20848587954         - double - 
    SMtoGEI : 1.0599030284
    GSEtoGSM : 0.000331975572344
    GSEtoSM : 0.219822175333        - double
    GSEtoMAG : 0.328390813522       - double
    GSEtoGEO : 0.220110928754       - double
    GSEtoGEI : 1.1531113136
    MAGtoGSM : 1.37525404825         - double - uses MAGSM SMGSW
    MAGtoSM : 7.15463008082e-05
    MAGtoGSE : 1.4642099926          - double 
    MAGtoGEO : 0.0003161328122
    MAGtoGEI : 1.07845017083         - double
    GEOtoGSM : 0.000259748696309
    GEOtoSM : 0.662392857954         - double
    GEOtoGSE : 1.17362395871        - double
    GEOtoMAG : 0.000172432969852
    GEOtoGEI : 2.06155857114e-12
    GEItoGSM : 1.20396615341         - double - uses GEOGSW GEIGEO
    GEItoSM : 0.394914270574
    GEItoGSE : 1.06287956704         - double
    GEItoMAG : 1.20384074267        - double
    GEItoGEO : 2.06155857114e-12

"""
        
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
