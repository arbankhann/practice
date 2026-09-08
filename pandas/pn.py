# import pandas as pd 
# print(pd.__version__)
# data={
#     "name":["ak","ik","wk"],
#     "roll no":[23,45,78]
# }
# showinfo=pd.DataFrame(data)
# print(showinfo)
# print(type(data))


# PANDAS SERIES IS LIKE A COLUMN OF THE TABLE
# s=[1,2,3,4]
# N=pd.Series(s)
# print(N[1])

# index
# a=[1,2,3]
# myval=pd.Series(a,index=["x","y","z"])
# print(myval)
# print(myval["z"])

# SIMPLE DICTINORI4ES
# data={
#     "day1":420,
#     "day2":456,
#     "day3":356
# }
# output=pd.Series(data)
# print(output)


# data1={
#     "name":["ak","wm"],
#     "roll_no":[2,1]
# }
# val=pd.DataFrame(data1)
# print(val)
# val=pd.DataFrame(data1,index=[11,12])
# print(val)


# data={
#     "day1":340,
#     "day2":234,
#     "day3":345
#  }
# val1=pd.Series(data,index=["day3","day1"])
# a=[1,2,3]
# val=pd.Series(a,index=["a","b","c"])
# print(val)



# Loc
# data={
#     "duration":[1,2,3,4,5],
#     "calories":[355,567,786,900,800]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print(df.loc[[0,3]])
# df=pd.DataFrame(data,index=["day1","day2","day3","day4","day5"])
# print(df.loc["day1"])

# n=pd.read_csv("_/ak.csv")
# n = pd.read_csv("pandas/ak.csv")
# print(n)
# print(n.to_string())

# number of rows
# import pandas as pd 
# print(pd.options.display.max_rows)

# No of rows increase
# pd.options.display.max_rows=999
# n=pd.read_csv("akk.csv")
# print(n)


# json
# m=pd.read_json("data.json")
# print(m)
# print(m.head(10))
# print(m.to_string())
# n=pd.read_csv("akk.csv")
# print(n.head(10))
# print(n.tail(10))
# print(n.info())


# a=pd.array([1,2,3,4,5])
# value=pd.Series(a,index=["x1","x2","x3","x4","x5"])
# print(value)

# a={
#     "number":[1,2,3,4,5],
#     "name:":["ak","zk","jk","nk","kk"]
# }
# value=pd.DataFrame(a)
# print(value)
# import numpy as np

# dice=np.random.choice([1,2,3,4,5,6],size=2)
# even=np.sum(dice%2==0)
# probability=even/2
# print(dice)
# print(even)
# print(probability)


import pandas as pd 
a={
    "name":["ak","jk","rk"],
    "roll_no":[1,2,3]
}
print(pd.Series(a))