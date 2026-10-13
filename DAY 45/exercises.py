import pandas as pd
import matplotlib.pyplot as plt

students = {
    "Name": ["Ali", "Sara", "Ahmed", "Zara", "Rehan",
             "Aisha", "Omar", "Fatima"],
    "Study_Hours": [2, 5, 3, 6, 1, 4, 2, 5],
    "Attendance": [65, 90, 75, 95, 55, 85, 60, 92],
    "Math": [55, 88, 70, 95, 40, 82, 50, 90],
    "Python": [60, 92, 68, 98, 45, 86, 55, 94],
    "English": [70, 85, 72, 90, 60, 88, 65, 91]
}

df = pd.DataFrame(students)

# Exercise 1: Inspect the dataset
print("First five rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Exercise 2: Calculate average marks
subjects = ["Math", "Python", "English"]
df["Average"] = df[subjects].mean(axis=1)

print("\nStudent averages:")
print(df[["Name", "Average"]])

# Exercise 3: Compare subjects
subject_averages = df[subjects].mean()

print("\nAverage marks by subject:")
print(subject_averages)

print("\nHighest-scoring subject on average:")
print(subject_averages.idxmax())

# Find students scoring at least 80 on average
print("\nStudents with average >= 80:")
print(df.loc[df["Average"] >= 80, ["Name", "Average"]])

# Exercise 4: Correlation analysis
correlation = df["Study_Hours"].corr(df["Average"])

print("\nStudy hours and average marks correlation:")
print(round(correlation, 3))

# Exercise 5: Scatter plot
plt.scatter(df["Study_Hours"], df["Average"])

plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.title("Study Hours vs Average Marks")
plt.grid(True)
plt.tight_layout()
plt.show()