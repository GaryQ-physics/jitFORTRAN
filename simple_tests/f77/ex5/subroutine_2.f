!#######################################################################
!#######   subroutine_2.f     ##########################################
!#######################################################################

!SUBV_2
      SUBROUTINE subV_2(x,N)
      IMPLICIT NONE
      INTEGER*8 N
      REAL*4 x(N)
!f2py intent(in) :: x
      INTEGER*8 ind

      DO 10 ind=1,N
        print*, 2.*x(ind)
10    CONTINUE
      END
