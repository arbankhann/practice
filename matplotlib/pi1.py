import matplotlib.pyplot as plt 
import numpy as np 
# x=np.array([10,40,80,100])
# plt.pie(x)
# plt.show()


# labels and start angle

# mylabels=np.array(["banana","mango","cherry","apple"])
# plt.pie(x,labels=mylabels,startangle=90)
# plt.show()


# EXPLODE AND SHADOW
# x=np.array([3,9,10,12])
# mylabels=np.array(["banana","mango","cherry","apple"])
# myexplode=[0.2,0,0,0]
# plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow=True)
# plt.show()


# COLORS
x=np.array([23,45,78,90])
mylabels=["A","B","C","D"]
colors1=["hotpink","blue","red","yellow"]
plt.pie(x,labels=mylabels,colors=colors1)
# plt.legend()
plt.legend(title="alphabet")
plt.show()