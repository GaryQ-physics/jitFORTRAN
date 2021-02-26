import os
import sys
import shutil

#os.system('f2py -c subroutine_1.f -m pymod')
#shutil.move('pymod.so', '/tmp/pymod.so')
#
#sys.path.append('/tmp/')
#import pymod
#exec('sub = pymod.subv_1')
#sys.path.remove('/tmp/')
#os.remove('/tmp/pymod.so')
#
#print('\n\n\n\n\n\n##########################################\n\n\n\n\n\n')
#
#os.system('f2py -c subroutine_2.f -m pymod')
#shutil.move('pymod.so', '/tmp/pymod.so')
#
#sys.path.append('/tmp/')
#import pymod
#exec('sub = pymod.subv_2')
#sys.path.remove('/tmp/')
#os.remove('/tmp/pymod.so')

works = False

if works:
    os.system('f2py -c subroutine_1.f -m pymod1')
    import pymod1
    sub = pymod1.subv_1
    os.remove('pymod1.so')

    print('\n\n\n\n\n\n##########################################\n\n\n\n\n\n')

    os.system('f2py -c subroutine_2.f -m pymod2')
    import pymod2
    sub = pymod2.subv_2
    os.remove('pymod2.so')
else:
    os.system('f2py -c subroutine_1.f -m pymod')
    import pymod
    sub = pymod.subv_1
    os.remove('pymod.so')
    del pymod
    del sub

    print('\n\n\n\n\n\n##########################################\n\n\n\n\n\n')

    os.system('f2py -c subroutine_2.f -m pymod')
    import pymod
    sub = pymod.subv_2
    os.remove('pymod.so')
