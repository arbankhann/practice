import pandas as pd 
# print(pd.__version__)
data={
    "name":["ak","ik","wk"],
    "roll no":[23,45,78]
}
showinfo=pd.DataFrame(data)
print(showinfo)
print(type(data))
s=[1,2,3,4]
print(pd.Series(s))
print(s[2])