# from scipy import constants 
# print(constants.liter)
# import scipy as sp 
# print(sp.constants.liter)
# print(sp.__version__)
# print(dir(sp.constants))
# print(sp.constants.kilo)
# print(sp.constants.zepto)
# print(sp.constants.deci)
# print(sp.constants.centi)
# print(sp.constants.year)
# print(sp.constants.week)
# print(sp.constants.day)
# print(sp.constants.hour)
# print(sp.constants.minute)
# print(sp.constants.inch)
# print(sp.constants.degree_Fahrenheit)






# optimizers solution
# from scipy.optimize import root
# from numpy import cos
# def eqn(x):
#     return x+cos(x)
# my_root=root(eqn,0)
# print(my_root.x)

# Minimize value
# from scipy.optimize import minimize 
# def eqn(x):
#     return x**2+x+2
# my_min=minimize(eqn,0,method='BFGS')
# print(my_min.x)

# maximize value 
# from scipy.optimize import minimize 
# def eqn(x):
#     return -(x**2+x+2)
# my_max=minimize(eqn,0,method='BFGS')
# print("maximum point",my_max.x)
# print("maximum value",-my_max.fun)





#SPARSE DATA 
# import numpy as np
# from scipy.sparse import csr_matrix 
# arr=np.array([1,2,3,0,0,0,0,0,4,5,0])
# print(csr_matrix(arr).count_nonzero())
# print(csr_matrix(arr).data)

# import numpy as np 
# from scipy.sparse import csr_matrix
# arr=np.array([[1,2,3],[4,5,0],[0,0,0]])
# print(csr_matrix(arr).data)
# print(csr_matrix(arr).count_nonzero())

# eliminate zeros 
# from scipy.sparse import csr_matrix 
# import numpy as np
# arr=np.array([[1,2,3],[4,0,0],[5,6,0]])
# mat=csr_matrix(arr)
# mat.eliminate_zeros()
# print(mat)


# sum_duplicate
# from scipy.sparse import csr_matrix
# import numpy as np 
# arr=np.array([[0,1,2],[0,0,9],[8,1,2]])
# mat=csr_matrix(arr)
# mat.sum_duplicates()
# print(mat)


# csr convert to csc with (.tocsc)

# from scipy.sparse import csr_matrix
# import numpy as np 
# arr =np.array([[1,0,9],[0,9,8],[0,0,2]])
# print(csr_matrix(arr).tocsc())


# graph
# connected components
# import numpy as np
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse import csr_matrix 
# arr=np.array([
#     [0,1,2],
#     [2,0,8],
#     [0,0,2],[0,0,0]])
# newarr=csr_matrix(arr)
# print(connected_components(newarr))


# dijiskra
# import numpy as np 
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import dijkstra
# arr=np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]
# ])
# dij=csr_matrix(arr)
# print(dijkstra(dij,return_predecessors=True,indices=0))


# floyed warshell
# import numpy as np 
# from scipy.sparse import csr_matrix 
# from scipy.sparse.csgraph import floyd_warshall 
# arr=np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]

# ])
# new=csr_matrix(arr)
# print(floyd_warshall(new))
# print(floyd_warshall(new,return_predecessors=True))


# DEpth first search 
# import numpy as np 
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import depth_first_order
# arr=np.array([
#     [1,2,3,0],
#     [2,7,0,0],
#     [2,0,9,0],
#     [2,0,9,0
# ]])
# dfo=csr_matrix(arr)
# print(depth_first_order(dfo,1))


# Breadth first order 
import numpy as np 
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order
arr=np.array([
    [1,2,3,0],
    [2,7,0,0],
    [2,0,9,0],
    [2,0,9,0]
])
bfo=csr_matrix(arr)
print(breadth_first_order(bfo,1))