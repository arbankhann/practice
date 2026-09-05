# EMPTY CELL 
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# new_df=df.dropna()
# print(new_df)
# print(new_df.to_string())

# EMPTY CELL ORIGINAL DATA
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# df.dropna(inplace=True)
# print(df)

# Replace empty value
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# df.fillna("ARban",inplace=True)
# print(df.to_string())


# replae with specific column
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# df.fillna({"n03":"ak"},inplace=True)
# print(df.to_string())
#

# REPLACE WITH MEAN
# import pandas as pd
# df=pd.read_csv("akk.csv")
# x=df["n02"].median()
# df.fillna({"n02":x},inplace=True)
# print(df.to_string())

# replace with median
# import pandas as pd
# df=pd.read_csv("akk.csv")
# x=df["n01"].median()
# df.fillna({"no1":x},inplace=True)
# print(df.to_string())

# replace with mode 
import pandas as pd
df=pd.read_csv("akk.csv")
x=df["n02"].mode()[0]
df.fillna({"n02":x},inplace=True)
print(df.to_string())