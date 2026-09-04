import numpy as np 
# x=np.array([1,2,3,4,5])
# h=0.0001
# f=lambda x:x**2
# def f(x):
#     return x**2
# derivaates=(f(x+h)-f(x))/h
# print(derivaates)


# import numpy as np 
# x=np.array([1,2,3,4,5])
# x=np.linspace(2,5,100)
# y=x**2
# dy_dx=np.gradient(y,x)
# print(dy_dx)

# import numpy as np

# x = np.array([1, 2, 3, 4, 5])

# y = x**2

# # dy_dx = np.gradient(y, x)
# dy_dx=2*x

# print(dy_dx)


#  Constant value
# import numpy as np:
# f = lambda x: x**2

# x = 3
# h = 0.0001

# derivative = (f(x + h) - f(x)) / h

# print(derivative)

# INTEGRATION 
# import numpy as np 
# x=np.linspace(0,5,100)
# y=x**2 
# area=np.trapz(y,x)
# print(area)


# x=np.array([1,2,3,4,5])
# y=x**2
# dy_dx=np.gradient(y,x)
# print(dy_dx)


x=np.linspace(0,5,100)
y=x**2
dy_dx=np.trapz(y,x)
print(dy_dx)



