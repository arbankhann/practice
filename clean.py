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
# import pandas as pd
# df=pd.read_csv("akk.csv")
# x=df["n02"].mode()[0]
# df.fillna({"n02":x},inplace=True)
# print(df.to_string())


# wrong format 
# import pandas as pd
# df=pd.read_csv("akk.csv")
# df['Date']=pd.to_datetime(df['Date'],format='mixed')
# print(df.to_string())

# Removing rows
# import pandas as pd

# df = pd.read_csv('akk.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# df.dropna(subset=['Date'], inplace = True)

# print(df.to_string())


# wrong data
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# df.loc[7,'Duration']="Arban"
# print(df.to_string())

# boundries /limit
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# for x in df.index:
#     df.loc[x,'Duration']>120
#     df.loc[x,'Duration']=120
# print(df.to_string())



# Duplicate value
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# print(df.duplicated())


# REmove duplicate value 
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# df.drop_duplicates(inplace=True)
# print(df.to_string())


# coreralation
# import pandas as pd 
# df=pd.read_csv("akk.csv")
# print(df.corr())



# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('akk.csv')

# df.plot()

# plt.show()
