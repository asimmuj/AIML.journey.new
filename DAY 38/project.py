
import pandas as pd

students = {
    "Name": [
        "Ali", "Sara", "John", "Mujtaba",
        "Zara", "Ahmed", "Ayesha", "Rahul",
        "Fatima", "David", "Hassan", "Priya"
    ],

    "Department": [
        "CSE", "ECE", "CSE", "ECE",
        "CSE", "ECE", "CSE", "ECE",
        "CSE", "ECE", "CSE", "ECE"
    ],

    "Python": [85, 90, 78, 88, 95, 75, 82, 91, 89, 76, 93, 87],

    "Maths": [80, 85, 75, 90, 92, 78, 88, 84, 86, 80, 91, 89],

    "DSA": [88, 82, 80, 85, 94, 79, 90, 87, 84, 77, 96, 92],

    "Attendance": [90, 85, 78, 92, 96, 80, 88, 91, 87, 75, 95, 89]
}
df = pd.DataFrame(students)
# Calculate average marks for each student
df["Average"] = df[["Python", "Maths", "DSA"]].mean(axis=1)
print("STUDENT PERFORMANCE REPORT")
print(df)
# Department-wise average marks
print("\nAverage marks by department:")
print(df.groupby("Department")["Average"].mean())
# Highest marks in each department
print("\nHighest marks:")
print(df.groupby("Department")["Average"].max())
# Lowest marks in each department
print("\nLowest marks:")
print(df.groupby("Department")["Average"].min())
# Number of students in each department
print("\nStudents in each department:")
print(df.groupby("Department")["Name"].count())
# Average attendance
print("\nAverage attendance:")
print(df.groupby("Department")["Attendance"].mean())
# Students scoring above 80
print("\nStudents scoring above 80:")
top_students = df[df["Average"] > 80]
print(top_students[["Name", "Department", "Average"]])
# Complete department-wise summary
print("\nDEPARTMENT SUMMARY")
print("-" * 40)
summary = df.groupby("Department").agg({
    "Average": ["mean", "max", "min"],
    "Attendance": "mean",
    "Name": "count"
})
print(summary)
# Department with highest average performance
department_scores = df.groupby("Department")["Average"].mean()
best_department = department_scores.idxmax()
print("\nDepartment with highest average performance:", best_department)
print("Average marks:", round(department_scores.max(), 2))