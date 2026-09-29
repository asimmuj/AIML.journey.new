# #exercise 1
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Mujtaba", "Zeeshan"],
#     "Age": [19, 20, 18, 21, 19],
#     "Department": ["CSE", "ECE", "CSE", "IT", "ECE"],
#     "Marks": [85, 92, 67, 78, 95],
#     "Attendance": [90, 95, 70, 82, 88]
# }
# df = pd.DataFrame(data)
# # Display only names
# print(df["Name"])
# # Display selected columns
# print(df[["Name", "Age", "Marks"]])
# # Display first three rows
# print(df.iloc[0:3])
# # Display last two rows
# print(df.iloc[-2:])

#exercise 2
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Mujtaba", "Zeeshan"],
#     "Age": [19, 20, 18, 21, 19],
#     "Department": ["CSE", "ECE", "CSE", "IT", "ECE"],
#     "Marks": [85, 92, 67, 78, 95],
#     "Attendance": [90, 95, 70, 82, 88]
# }
# df = pd.DataFrame(data)
# # Students scoring more than 85
# print("Students scoring above 85:")
# print(df[df["Marks"] > 85])
# # Students with attendance below 85
# print("\nStudents with low attendance:")
# print(df[df["Attendance"] < 85])
# # Students belonging to ECE
# print("\nECE students:")
# print(df[df["Department"] == "ECE"])
# # Students aged 19 or above
# print("\nStudents aged 19 or above:")
# print(df[df["Age"] >= 19])
# # Students scoring between 75 and 95
# print("\nStudents scoring between 75 and 95:")
# print(df[df["Marks"].between(75, 95)])

#exercise 3
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Mujtaba", "Zeeshan"],
#     "Age": [19, 20, 18, 21, 19],
#     "Department": ["CSE", "ECE", "CSE", "IT", "ECE"],
#     "Marks": [85, 92, 67, 78, 95],
#     "Attendance": [90, 95, 70, 82, 88]
# }
# df = pd.DataFrame(data)
# # Marks above 80 AND attendance above 85
# print("High marks and attendance:")
# print(df[(df["Marks"] > 80) & (df["Attendance"] > 85)])
# # Marks below 70 OR attendance below 80
# print("\nLow marks or attendance:")
# print(df[(df["Marks"] < 70) | (df["Attendance"] < 80)])
# # CSE or ECE students scoring above 80
# print("\nCSE/ECE students scoring above 80:")
# print(df[
#     (df["Department"].isin(["CSE", "ECE"])) &
#     (df["Marks"] > 80)
# ])
# # Students who do not belong to IT
# print("\nStudents outside IT:")
# print(df[df["Department"] != "IT"])

#exercise 4
# import pandas as pd
# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Mujtaba", "Zeeshan"],
#     "Age": [19, 20, 18, 21, 19],
#     "Department": ["CSE", "ECE", "CSE", "IT", "ECE"],
#     "Marks": [85, 92, 67, 78, 95],
#     "Attendance": [90, 95, 70, 82, 88]
# }
# df = pd.DataFrame(data)
# # Sort marks in ascending order
# print("Marks in ascending order:")
# print(df.sort_values(by="Marks"))
# # Sort attendance in descending order
# print("\nAttendance in descending order:")
# print(df.sort_values(by="Attendance", ascending=False))
# # Sort by department and then marks
# print("\nSorted by department and marks:")
# print(df.sort_values(
#     by=["Department", "Marks"],
#     ascending=[True, False]
# ))
# # Display top three students
# print("\nTop three students:")
# print(df.sort_values(by="Marks", ascending=False).head(3))
# # Use loc to select students scoring above 80
# print("\nStudents scoring above 80:")
# print(df.loc[df["Marks"] > 80, ["Name", "Marks"]])