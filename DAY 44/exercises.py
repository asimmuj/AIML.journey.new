import pandas as pd
data = {
    "student": ["Ali", "Sara", "Ahmed", "Zoya", "Mujtaba",
                "Aman", "Ayesha", "Rohan", "Fatima", "Kabir"],
    "study_hours": [2, 5, 3, 7, 4, 1, 6, 3, 8, 2],
    "attendance": [65, 90, 75, 95, 80, 50, 92, 70, 98, 60],
    "marks": [45, 82, 58, 94, 72, 35, 88, 55, 97, 42]
}
df = pd.DataFrame(data)
print("Number of students:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Average attendance:", df["attendance"].mean())
print("Median marks:", df["marks"].median())

import pandas as pd
data = {
    "student": ["Ali", "Sara", "Ahmed", "Zoya", "Mujtaba"],
    "marks": [45, 82, 58, 94, 72]
}
df = pd.DataFrame(data)
# Add a missing mark
df.loc[2, "marks"] = None
# Add a duplicate row
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("Dataset:")
print(df)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())