import pandas as pd
data=pd.read_csv("students.csv")
df=pd.DataFrame(data)
print(df)
total=len(df)
print("total students:", total)
passed=df[df["Marks"]>40]
print("passed students:", passed)
failed=df[df["Marks"]<40]
print("failed students:", failed)