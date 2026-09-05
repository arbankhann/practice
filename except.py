# import numpy as np 
# A=np.array([1,2,3])
# B=np.array([0.2,0.5,0.3])
# ECXEPTION=np.sum(A*B)
# print(ECXEPTION)

import numpy as np 
from statistics import mode
V=np.array([1,2,3,4,5,6,6])
# print(np.var(V))
# print(np.mean(V))
print(np.median(V))
mode1=mode(V)
print(mode1)

a=[1,2,3,4,5]
mean_value=np.mean(a)
print(mean_value)
median_value=np.median(a)
print(median_value)