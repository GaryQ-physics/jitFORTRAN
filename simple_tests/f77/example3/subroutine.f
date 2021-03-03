      SUBROUTINE subV(x,N)
      IMPLICIT NONE
      INTEGER*8 N
      REAL*4 x(N)
      INTEGER*8 ind

      DO 10 ind=1,N
        call sub(x(ind))
10    CONTINUE
      END
      INCLUDE 'sub.f'
