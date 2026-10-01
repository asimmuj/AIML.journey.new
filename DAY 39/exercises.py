# #exercise 1
# import pandas as pd
# import numpy as np
# students = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zoya", "Rohan"],
#     "Age": [19, np.nan, 20, 18, np.nan],
#     "Marks": [85, 90, np.nan, 76, 88]
# }
# df = pd.DataFrame(students)
# print("Student Data:")
# print(df)
# print("\nMissing values in each column:")
# print(df.isnull().sum())
# print("\nTotal missing values:")
# print(df.isnull().sum().sum())

#exercise 2
# import pandas as pd
# import numpy as np
# employees = {
#     "Employee": ["Ali", "Sara", "Ahmed", "Zoya", "Rohan"],
#     "Salary": [25000, 30000, np.nan, 28000, 35000],
#     "Department": ["IT", "HR", "IT", np.nan, "Sales"]
# }
# df = pd.DataFrame(employees)
# print("Original Data:")
# print(df)
# df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# df["Department"] = df["Department"].fillna(df["Department"].mode()[0])
# print("\nAfter filling missing values:")
# print(df)
# print("\nRemaining missing values:")
# print(df.isnull().sum())

#exercise 3
# import pandas as pd
# students = {
#     "Name": ["Ali", "Sara", "Ahmed", "Ali", "Zoya", "Sara"],
#     "Age": [19, 20, 21, 19, 18, 20],
#     "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Jaipur", "Mumbai"]
# }
# df = pd.DataFrame(students)
# print("Original Data:")
# print(df)
# print("\nDuplicate records:")
# print(df[df.duplicated()])
# print("\nTotal duplicate records:")
# print(df.duplicated().sum())
# df = df.drop_duplicates()
# print("\nAfter removing duplicates:")
# print(df)

# #exercise 4
# import pandas as pd
# import numpy as np
# students = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zoya", "Rohan", "Ali", "Neha"],
#     "Age": [19, 20, np.nan, 18, 21, 19, np.nan],
#     "Marks": [85, 90, 78, np.nan, 88, 85, 92],
#     "City": ["Delhi", "Mumbai", "Delhi", np.nan, "Pune", "Delhi", "Mumbai"]
# }
# df = pd.DataFrame(students)
# print("Original Dataset:")
# print(df)
# print("\nMissing values:")
# print(df.isnull().sum())
# print("\nDuplicate records:", df.duplicated().sum())
# # Remove duplicate rows
# df = df.drop_duplicates()
# # Fill missing values
# df["Age"] = df["Age"].fillna(df["Age"].median())
# df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# df["City"] = df["City"].fillna(df["City"].mode()[0])
# print("\nCleaned Dataset:")
# print(df)
# print("\nFinal missing values:")
# print(df.isnull().sum())
# print("\nFinal duplicate records:", df.duplicated().sum())