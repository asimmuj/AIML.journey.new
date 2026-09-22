import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Zain", "Maya",
             "Omar", "Aisha", "Hamza", "Noor", "Yusuf"],

    "Age": [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],

    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE",
                   "CSE", "CSE", "ECE", "CSE", "ECE"],

    "Math": [85, 92, 76, 88, 65, 95, 82, 70, 90, 78],

    "Python": [90, 95, 72, 85, 68, 91, 88, 75, 94, 80],

    "DSA": [80, 89, 70, 92, 60, 96, 85, 72, 91, 76]
}
df = pd.DataFrame(data)
print("Student Data:")
print(df)
print("\nShape of data:", df.shape)
print("\nColumn names:")
print(df.columns)
print("\nAverage marks:")
print("Math:", df["Math"].mean())
print("Python:", df["Python"].mean())
print("DSA:", df["DSA"].mean())
# calculating total and average marks
df["Total"] = df["Math"] + df["Python"] + df["DSA"]
df["Average"] = df["Total"] / 3
# checking whether the student passed
df["Passed"] = df["Average"] >= 40
print("\nUpdated student data:")
print(df)
# finding the student with the highest average
top_student = df.loc[df["Average"].idxmax()]
print("\nTop student:")
print(top_student["Name"])
print("Average:", top_student["Average"])
# students who scored 80 or more
print("\nStudents with average 80 or more:")
print(df[df["Average"] >= 80][["Name", "Average"]])
# sorting students according to their average
print("\nStudents ranked by average:")
print(df.sort_values("Average", ascending=False)[["Name", "Average"]])
def get_performance(average):
    if average >= 90:
        return "Excellent"
    elif average >= 75:
        return "Good"
    elif average >= 60:
        return "Average"
    else:
        return "Poor"
df["Performance"] = df["Average"].apply(get_performance)
print("\nFinal report:")
print(df[["Name", "Department", "Total",
          "Average", "Passed", "Performance"]])