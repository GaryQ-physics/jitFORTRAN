import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
import jitFORTRAN

N=10
x = np.arange(N, dtype=np.float32)


with open('subroutine_2.f', 'r') as include:
    script = ''.join(include.readlines())

subrt_2 = jitFORTRAN.Fortran_Subroutine(script, 'subV_2')
subrt_2.execute(x, N)

if False:
    print('reex')
    subrt_2.execute(x, N)
