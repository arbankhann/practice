# PLOTING X AND Y POINT  with line 
# import matplotlib.pyplot as plt
# import numpy as np 
# xpoint=np.array([1,8])
# ypoint=np.array([3,10])
# plt.plot(xpoint,ypoint)
# plt.show()



#PLOTING POINT WITHOUT LINE 
# import numpy as np
# import matplotlib.pyplot as plt 
# xpoint=np.array([1,3])
# ypoint=np.array([8,10])
# plt.plot(xpoint,ypoint,marker='o')
# plt.show() 


# multiple points
# import numpy as np 
# import matplotlib.pyplot as plt 
# xpoint=np.array([1,2,6,8])
# ypoint=np.array([3,8,1,10])
# plt.plot(xpoint,ypoint)
# plt.show()

# DEfault x point 
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoint=([3,6,3,10]) 
# plt.plot(ypoint)
# plt.show()

# Maarker each point of the circle 
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoint=([3,5,0,9,8])
# plt.plot(ypoint,marker="P")
# plt.plot(ypoint,'o:b')
# plt.show()

# differnt type of line 
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoint=np.array([2,8,0,4])
# plt.plot(ypoint,'o-')
# plt.plot(ypoint,'o:')
# plt.plot(ypoint,'--')
# plt.plot(ypoint,'o:k')
# plt.show()

# MARKER SIZE 
# import numpy as np 
# import matplotlib.pyplot as plt 
# ypoint=np.array([3,8,9,0])
# plt.plot(ypoint,marker='o',ms=30)
# plt.plot(ypoint,marker='*',ms=20,mec='r',mfc='y')
# plt.show()

# LINESTYLE
# import matplotlib.pyplot as plt 
# import numpy as np 
# ypoint=np.array([3,7,8,0,2])
# plt.plot(ypoint,linestyle="dotted")
# plt.plot(ypoint,'o:')
# plt.plot(ypoint,linestyle="dashed")
# plt.plot(ypoint,ls='dotted')
# plt.show()

# LINE COLOR 
# import matplotlib.pyplot as plt 
# import numpy as np 
# ypoint=np.array([3,0,9,8])
# plt.plot(ypoint,color='r')
# plt.show()

# Line width 
# import matplotlib.pyplot as plt
# n=([1,2,3,4])
# plt.plot(n,lw=5)
# plt.show()
#


# MULTIPLE LINE
# import numpy as np 
# import matplotlib.pyplot as plt 
# y=np.array([1,4,5,6,4])
# x=np.array([2,4,6,8,0])
# plt.plot(y,lw=5)
# plt.plot(x,lw=10)
# plt.show()


# multiple line for both axis 
# import matplotlib.pyplot as plt 
# import numpy as np
# x1=np.array([1,9,8])
# y1=np.array([2,0,9])
# x2=np.array([0,9,8])
# y2=np.array([4,7,8])
# plt.plot([x1,y1,x2,y2])
# plt.show()



# Create labels for plot 
# import matplotlib.pyplot as plt 
# import numpy as np 
# xpoint=np.array([2,9,7,5,3])
# ypoint=np.array([3,9,8,2,1])
# plt.plot(xpoint,ypoint)
# plt.title("graph",loc="left")
# plt.xlabel("Average plus")
# plt.ylabel("Calories")
# plt.show()


#LABELLING 

# import matplotlib.pyplot as plt 
# import numpy as np 
# xpoint=np.array([1,2,4,5,8,2])
# ypoint=np.array([3,5,4,8,6,2])
# font1={"family":"sarif","color":"red","size":20}
# font2={"family":"sarif","color":"blue","size":15}
# plt.title("GRAPH",fontdict=font1)
# plt.xlabel("x-asis",fontdict=font2)
# plt.ylabel("y-asix",fontdict=font2)
# plt.plot(xpoint,ypoint)
# plt.show()

# ADD GRID LINES TO A STACK 
# import matplotlib.pyplot as plt 
# import numpy as np 
# x=np.array([2,4,6,7,8,9,2])
# y=np.array([3,6,9,12,6,8,6])
# plt.title("HEADING:Student Data",loc="right",c='red',size=20)
# plt.xlabel("x-asis")
# plt.ylabel("Y-axis")
# plt.plot(x,y,marker='o',markersize=15)
# both x asis and y asis
# plt.grid()


# properties
# plt.grid(color="black",linestyle="--",linewidth=0.9)
# support x asis
# plt.grid(axis='x')

# support y asix
# plt.grid(axis='y')
# plt.show()



# DISPLAY MULTIPLE SUBPLOT 
# import matplotlib.pyplot as plt 
# import numpy as np 
# x=np.array([2,4,5,6])
# y=np.array([4,7,9,10])
# plt.subplot(1,2,1)
# plt.plot(x,y)
# x=np.array([2,3,4,5])
# y=np.array([3,4,6,7])
# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.show()



# DISPLAY MULTIPLE GRAPH 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)
# plt.title("FIRST")

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)
# plt.title("SECOND")

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)
# plt.plot("THIRD")

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)
# plt.title("FOURTH")

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)
# plt.title("FIFTH")

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)
# plt.title("SIXTH")
# plt.xlabel("x-ais")
# plt.ylabel("y-axis")

# plt.show()

# SCatter plot 
# import numpy as np 
# import matplotlib.pyplot as plt 
# x=np.array([2,6,8,9,4])
# y=np.array([6,8,4,9,5])
# plt.scatter(x,y)
# plt.show()

#  Compair plots 
# import matplotlib.pyplot as plt
# import numpy as np

#day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y,c='black')

#day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()


# COLORS OF EACH DOT 
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# plt.scatter(x, y, color=colors)

# plt.show()


#  USE COLOR MAP USING VIRIDIS 
# import matplotlib.pyplot as plt 
# import numpy as np 
# x=np.array([2,5,7,9])
# y=np.array([4,8,9,10])
# colors=np.array([0,20,30,100])
# plt.scatter(x,y,cmap="viridis")
# plt.show()

# SIZES
# import matplotlib.pyplot as plt 
# import numpy as np 
# x=np.array([2,7,8,9,10,9])
# y=np.array([6,9,8,6,10,9])
# sizes=np.array([10,90,100,5,900,76])
# plt.scatter(x,y,s=sizes,alpha=0.5)
# plt.colorbar()
# plt.show()

# combine color size with alpha 
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

plt.colorbar()

plt.show()