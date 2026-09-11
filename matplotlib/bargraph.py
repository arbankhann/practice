# import matplotlib.pyplot as plt
# import numpy as np 
# x=np.array([4,5,6,8,7,9,10])
# y=np.array([8,10,12,16,14,18,20])
# graph normal
# plt.bar(x,y)
# horizanta
# plt.barh(x,y,color="yellow")
# colors
# plt.bar(x,y,color="red")
# bar width 
# plt.bar(x,y,width=0.10)
# height
# plt.barh(x,y,color="pink",height=0.1,align="center")
# plt.show() 


# HISTOGRAM
import numpy as np 
import matplotlib.pyplot as plt 
x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()