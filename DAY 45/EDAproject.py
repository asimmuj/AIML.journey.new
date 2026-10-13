import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create the dataset
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

subjects = ["Math", "Python", "English"]

# Create a folder for charts and output files
os.makedirs("images", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 2. Inspect the dataset
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 35)

print("\nFirst five rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nStatistical summary:")
print(df.describe())

# 3. Check and clean the data
df = df.drop_duplicates().copy()

# Check for missing values before calculating averages
df[subjects] = df[subjects].apply(
    pd.to_numeric, errors="coerce"
)

# Marks should be between 0 and 100
invalid_marks = (
    (df[subjects] < 0) | (df[subjects] > 100)
).any(axis=1)

if invalid_marks.any():
    print("\nWarning: Invalid marks found.")
    print(df.loc[invalid_marks, ["Name"] + subjects])

# Calculate averages only when all three subject marks exist
df["Average"] = df[subjects].mean(axis=1)

print("\nStudents with missing subject marks:")
print(df[df[subjects].isnull().any(axis=1)])

# 4. Analyze student performance
print("\nAverage marks by subject:")
subject_averages = df[subjects].mean()
print(subject_averages.round(2))

print("\nHighest average:")
print(df.loc[df["Average"].idxmax(), ["Name", "Average"]])

print("\nLowest average:")
print(df.loc[df["Average"].idxmin(), ["Name", "Average"]])

print("\nStudents scoring at least 80:")
print(
    df.loc[df["Average"] >= 80, ["Name", "Average"]]
)

print("\nOverall average marks:", round(df["Average"].mean(), 2))

# 5. Study hours and marks correlation
correlation = df["Study_Hours"].corr(df["Average"])

print("\nCorrelation between study hours and average marks:")
print(round(correlation, 3))

# 6. Visualization 1: Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Average"], bins=5, edgecolor="black")

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("images/average_distribution.png")
plt.close()

# 7. Visualization 2: Subject comparison
plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar", edgecolor="black")

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/subject_comparison.png")
plt.close()

# 8. Visualization 3: Study hours vs marks
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Study_Hours"],
    df["Average"],
    s=80
)

plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/study_hours_vs_marks.png")
plt.close()

# 9. Visualization 4: Correlation heatmap
numeric_data = df[
    ["Study_Hours", "Attendance", "Math", "Python", "English", "Average"]
]

plt.figure(figsize=(9, 6))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.close()

# 10. Generate findings
print("\nPROJECT FINDINGS")
print("=" * 35)

print(
    f"1. Overall average marks: "
    f"{df['Average'].mean():.2f}"
)

print(
    f"2. Highest average: "
    f"{df.loc[df['Average'].idxmax(), 'Name']}"
)

print(
    f"3. Lowest average: "
    f"{df.loc[df['Average'].idxmin(), 'Name']}"
)

print(
    f"4. Highest-scoring subject on average: "
    f"{subject_averages.idxmax()}"
)

print(
    f"5. Study hours vs marks correlation: "
    f"{correlation:.3f}"
)

# 11. Save the results
df.to_csv("data/student_analysis_results.csv", index=False)

print("\nCharts saved in the images folder.")
print("Results saved in the data folder.")
print("Analysis completed!")
#done