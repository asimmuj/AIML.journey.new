import pandas as pd
import numpy as np
students = {
    "Name": ["Ali", "Sara", "Ahmed", "Zoya", "Rohan", "Neha", "Ali", "Aman", "Priya", "Sara"],
    "Age": [19, 20, np.nan, 18, 21, 19, 19, np.nan, 20, 20],
    "Marks": [85, 90, 78, np.nan, 88, 92, 85, 76, np.nan, 90],
    "City": ["Delhi", "Mumbai", "Delhi", np.nan, "Pune", "Jaipur", "Delhi", "Mumbai", np.nan, "Mumbai"]
}
df = pd.DataFrame(students)
print("Student Data")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Records:", df.duplicated().sum())
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
print("\nAfter Cleaning:")
print(df)
print("\nChecking Missing Values:")
print(df.isnull().sum())
print("\nChecking Duplicates:")
print(df.duplicated().sum())
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned data saved successfully!")