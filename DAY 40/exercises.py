# import pandas as pd
# df = pd.read_csv("students_raw.csv")
# print("First 5 rows:")
# print(df.head())
# print("\nDataset shape:")
# print(df.shape)
# print("\nColumn names:")
# print(df.columns)
# print("\nData types:")
# print(df.dtypes)
# print("\nMissing values:")
# print(df.isnull().sum())

#exercise 2
# import pandas as pd
# df = pd.read_csv("students_raw.csv")
# print("Duplicates before cleaning:", df.duplicated().sum())
# df = df.drop_duplicates()
# print("Duplicates after cleaning:", df.duplicated().sum())
# print("\nCleaned data:")
# print(df)

# #exercise 3
# import pandas as pd
# df = pd.read_csv("students_raw.csv")
# df["age"] = pd.to_numeric(df["age"], errors="coerce")
# df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
# df["age"] = df["age"].fillna(df["age"].median())
# df["marks"] = df["marks"].fillna(df["marks"].mean())
# df["city"] = df["city"].fillna("Unknown")
# print(df)
# print("\nMissing values after cleaning:")
# print(df.isnull().sum())

#exercise 4
# import pandas as pd
# df = pd.read_csv("students_raw.csv")
# df["city"] = df["city"].str.strip().str.title()
# df["department"] = df["department"].str.strip().str.upper()
# df["age"] = pd.to_numeric(df["age"], errors="coerce")
# df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
# print(df)
# print("\nData types:")
# print(df.dtypes)

#exercise 5
import pandas as pd
df = pd.read_csv("students_raw.csv")
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
invalid_marks = df[(df["marks"] < 0) | (df["marks"] > 100)]
print("Invalid marks:")
print(invalid_marks)
print("\nNumber of invalid records:", len(invalid_marks))
# Replace invalid marks with NaN
df.loc[(df["marks"] < 0) | (df["marks"] > 100), "marks"] = float("nan")
print("\nMarks after validation:")
print(df[["name", "marks"]])