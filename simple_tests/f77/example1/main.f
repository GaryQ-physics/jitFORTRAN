      PROGRAM main
      IMPLICIT NONE
C     is this really fortran 77 ?
      INTEGER*8, PARAMETER :: N = 5
C     PARAMETER (N=5) # https://web.stanford.edu/class/me200c/tutorial_77/05_variables.html
      REAL*4 x(N)
      x = (/ 0., 1., 2., 3., 4. /)
  
      CALL subV(x, N)
      END
 
      INCLUDE 'subroutine.f'
