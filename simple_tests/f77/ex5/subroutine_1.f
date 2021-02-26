!#######################################################################
!#######   subroutine_1.f     ##########################################
!#######################################################################

!SUBV_1
      SUBROUTINE subV_1(x,N)
      IMPLICIT NONE
      INTEGER*8 N
      REAL*4 x(N)
!f2py intent(in) :: x
      INTEGER*8 ind

      DO 10 ind=1,N
        print*, x(ind)
10    CONTINUE
      END
