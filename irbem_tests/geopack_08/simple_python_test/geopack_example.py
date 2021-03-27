# an example of using the GEOMAG_08 subroutine in geopack.f (from irbem).
# first, a fortran subroutine that takes arrays is used to wrap GEOMAG_08.
# then it is passed to jitFORTRAN.
import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
import jitFORTRAN

wrapper_subroutine_name='GEOMAG_08_V'
wrapper_script = '''!GEOMAG_08_V
      SUBROUTINE GEOMAG_08_V(XGEO_V,YGEO_V,ZGEO_V,XMAG_V,YMAG_V,ZMAG_V,
     1                       J,
     2                       IYEAR,IDAY,IHOUR,MIN,ISEC,
     3                       N)
C          vectorizes GEOMAG_08

C-----time of coordinate transform:
C     IYEAR   -  YEAR NUMBER (FOUR DIGITS)
C     IDAY  -  DAY OF YEAR (DAY 1 = JAN 1)
C     IHOUR -  HOUR OF DAY (00 TO 23)
C     MIN   -  MINUTE OF HOUR (00 TO 59)
C     ISEC  -  SECONDS OF MINUTE (00 TO 59)

C                    J>0                       J<0
C-----INPUT:  J,XGEO,YGEO,ZGEO           J,XMAG,YMAG,ZMAG
C-----OUTPUT:    XMAG,YMAG,ZMAG           XGEO,YGEO,ZGEO

      IMPLICIT NONE
C inputed dimension of arrays
      INTEGER*8 N
      REAL*8  XGEO_V(N), YGEO_V(N), ZGEO_V(N)
!f2py intent(in,out) ::  XGEO_V, YGEO_V, ZGEO_V
      REAL*8  XMAG_V(N), YMAG_V(N), ZMAG_V(N)
!f2py intent(in,out) ::  XMAG_V, YMAG_V, ZMAG_V
      INTEGER*4 J, IYEAR,IDAY,IHOUR,MIN,ISEC
      INTEGER*8 ind

C  RECALC_08 prepares elements of rot matrix and puts in common block
C  note since GEO and MAG are independent of solar wind, set 
C   can set VGSEX=-400.0, VGSEY=0.0, VGSEZ=0.0
      CALL RECALC_08(IYEAR,IDAY,IHOUR,MIN,ISEC,-4.0d2,0.0d0,0.0d0)

      DO 10 ind=1,N
      CALL GEOMAG_08(XGEO_V(ind),YGEO_V(ind),ZGEO_V(ind),
     1               XMAG_V(ind),YMAG_V(ind),ZMAG_V(ind), J)
10    CONTINUE
      END
'''


geomag_08_V_F = jitFORTRAN.Fortran_Subroutine(wrapper_script, 
                                              wrapper_subroutine_name,
                                              include='geopack_08')

IYEAR = 1
IDAY = 1
IHOUR = 1
MIN = 1
ISEC = 1

J = 1

N = 5
XGEO_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)
YGEO_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)
ZGEO_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)
XMAG_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)
YMAG_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)
ZMAG_V = np.array( [0., 1., 2., 3., 4.] , dtype=np.float64)

print(XGEO_V)
print(YGEO_V)
print(ZGEO_V)
print(XMAG_V)
print(YMAG_V)
print(ZMAG_V)

geomag_08_V_F.execute(XGEO_V,YGEO_V,ZGEO_V,XMAG_V,YMAG_V,ZMAG_V,
                    J,
                    IYEAR,IDAY,IHOUR,MIN,ISEC,
                    N)

print(XGEO_V)
print(YGEO_V)
print(ZGEO_V)
print(XMAG_V)
print(YMAG_V)
print(ZMAG_V)


