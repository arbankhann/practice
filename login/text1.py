import pandas as pd 
# a=[1,2,4,5,7,8]
# my_var=pd.Series(a,index=["x","y","z","k","l","m"])
# print(my_var)
# print(my_var["z"])
# data={
#     "name":["ak","ik","jk"],
#     "roll_no":[1,2,3]
# }
# data_val=pd.DataFrame(data)
# print(data_val)
# print(data_val["name"])
# print(data_val.loc[0])

df=pd.read_csv("akk.csv")
# print(df.to_string())
# print(pd.options.display.min_rows)

# pd.options.display.max_rows=1000
# df=pd.read_csv("akk.csv")
# print(df)
print(df.head(10))

# df=pd.read_json("data.json")
# print(df)