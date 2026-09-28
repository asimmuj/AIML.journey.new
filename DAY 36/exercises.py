# #exercise 1&2
# import pandas as pd
# df=pd.read_csv("titanic.csv")
# print(df)
# print(df.head(3))
# print(df.tail(2))
# print(df.shape)
# print(df.info())

#exercise 3
import pandas as pd
df=pd.read_csv("titanic.csv",usecols=["Name", "Age"])
print(df)
df.to_csv("updated_titanic.csv", index=False)