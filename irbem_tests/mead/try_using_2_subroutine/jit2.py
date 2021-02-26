import os
import sys
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
import jitFORTRAN

with open('outer_sub.f', 'r') as include:
    script = ''.join(include.readlines())

#print(script)

meadV_F = jitFORTRAN.Fortran_Subroutine(script, 'MEADV', include='sub')

n=100

xax = np.linspace(-20., 10., n)
zax = np.linspace(-15., 15., n)
x, z = np.meshgrid(xax,zax)

x = x.ravel()
z = z.ravel()
y = np.zeros(n**2, dtype=np.float64)

b1x = np.nan*np.empty((n**2,), dtype=np.float64)
b1y = np.nan*np.empty((n**2,), dtype=np.float64)
b1z = np.nan*np.empty((n**2,), dtype=np.float64)

meadV_F.execute(x, y, z, 1, b1x, b1y, b1z, n**2)

def B0(X): # dipole field
    M = np.array([0,0,3.12e+4], dtype=np.float32)#, dtype=np.float32) # "dipole moment"(not really) in  nT * R_e**3  # https://en.wikipedia.org/wiki/Dipole_model_of_the_Earth%27s_magnetic_field

    if X.shape == (3,):
        divr = 1./np.linalg.norm(X)
        if divr > 0.66667:
            return np.zeros(3)
        return ( 3.*np.dot(M,X)*divr**5 )* X  -  (divr**3) * M

    ret = np.nan*np.empty(X.shape)
    for i in range(X.shape[0]):
        ret[i,:] = B0(X[i,:])
    return ret[:,0],ret[:,1],ret[:,2]

b0x,b0y,b0z = B0(np.column_stack([x,y,z]))

#print(bx, by, bz)
bx = b0x + b1x
by = b0y + b1y
bz = b0z + b1z
norm_b = np.sqrt(bx**2 + by**2 + bz**2)

import matplotlib.pyplot as plt
#plt.imshow(norm_b.reshape((n,n)))
plt.pcolor(x.reshape((n,n)), z.reshape((n,n)), np.log10(norm_b).reshape((n,n)))
plt.colorbar()
plt.show()
