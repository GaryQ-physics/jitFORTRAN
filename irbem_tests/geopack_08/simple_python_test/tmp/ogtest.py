import numpy as np
import geopy

date = np.array((2000,1,0,0,0))
xi = np.arange(0,3,dtype=np.int64)
yi = np.arange(0,3,dtype=np.int64)
zi = np.arange(0,3,dtype=np.int64)

trans = "SMtoGSM"
ans = geopy.gptransform(xi,yi,zi,trans,date)
for a in ans:
	print(a)


