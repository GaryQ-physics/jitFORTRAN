!#######################################################################
!#######   main.f     ##########################################
!#######################################################################

      PROGRAM MAIN
      IMPLICIT NONE
      INTEGER*8, PARAMETER :: N = 1E9
      REAL*4 XV(N)
      INTEGER*8 ind
      REAL*4 start, finish

c     initialize input array xv
      DO 10 ind=1,N
        xv(ind) = 1./ind
10    CONTINUE

c     print preview of input
      print*, XV(1)
      print*, XV(1)
      print*, "..."
      print*, XV(N-1)
      print*, XV(N)

c     run through subroutine
      call cpu_time(start)
      CALL subV(XV,
     1            N
     2              )
      call cpu_time(finish)

c     print preview of output
      print*, XV(1)
      print*, XV(1)
      print*, "..."
      print*, XV(N-1)
      print*, XV(N)

      print*,N," points computed in ",finish-start," seconds"

      END

!SUBV
      SUBROUTINE subV(XV,N)
      IMPLICIT NONE
      INTEGER*8 N
      REAL*4 XV(N)
!f2py intent(in) :: x
      INTEGER*8 ind

      DO 20 ind=1,N
        call sub(XV(ind))
20    CONTINUE
      END
