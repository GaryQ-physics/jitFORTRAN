      PROGRAM main
      IMPLICIT NONE
      INTEGER*8, PARAMETER :: N = 5
      REAL*4 x(N)
      x = (/ 0., 1., 2., 3., 4. /)
  
      CALL subV(x, N)
      END
 
      INCLUDE 'subroutine.f'
