import numpy as np 
a=np.array(90)
print(a)
v=np.array([1,2,3])
print(v)
m=np.array([
    [1,2],
    [2,3]
])
n=np.array([
    [2,4],
    [4,6]
])q
c=m@n
print("mutiplication",c)
d=np.linalg.det(m)
print(d)

