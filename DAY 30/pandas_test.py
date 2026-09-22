#exercise 1
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zain", "Maya", "Omar"],
#     "Age": [20, 21, 19, 22, 20, 21],
#     "Marks": [85, 92, 76, 88, 65, 95],
#     "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"]
# }
# df = pd.DataFrame(data)
# print("Complete DataFrame:")
# print(df)
# print("\nFirst 3 rows:")
# print(df.head(3))
# print("\nShape:")
# print(df.shape)
# print("\nColumns:")
# print(df.columns)
# print("\nData Types:")
# print(df.dtypes)

#exercise 2
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zain", "Maya", "Omar"],
#     "Age": [20, 21, 19, 22, 20, 21],
#     "Marks": [85, 92, 76, 88, 65, 95],
#     "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"]
# }
# df = pd.DataFrame(data)
# print("Students with marks greater than 80:")
# print(df[df["Marks"] > 80])
# print("\nStudents older than 20:")
# print(df[df["Age"] > 20])
# print("\nCSE students:")
# print(df[df["Department"] == "CSE"])
# print("\nStudents with marks between 60 and 90:")
# print(df[(df["Marks"] >= 60) & (df["Marks"] <= 90)])

# #exercise 3
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zain", "Maya", "Omar"],
#     "Marks": [85, 92, 76, 88, 65, 95]
# }
# df = pd.DataFrame(data)
# average = df["Marks"].mean()
# highest = df["Marks"].max()
# lowest = df["Marks"].min()
# total = df["Marks"].sum()
# print("Average marks:", average)
# print("Highest marks:", highest)
# print("Lowest marks:", lowest)
# print("Total marks:", total)
# top_student = df.loc[df["Marks"].idxmax()]#idxmax() finds the index of the maximim value
# print("\nTop Student:")
# print(top_student)

#exercise 4
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zain", "Maya", "Omar"],
    "Marks": [85, 92, 76, 88, 65, 95]
}

df = pd.DataFrame(data)

# Create Passed column
df["Passed"] = df["Marks"] >= 40


# Function to assign grades
# def get_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"
# # Create Grade column
# df["Grade"] = df["Marks"].apply(get_grade)
##print(df)