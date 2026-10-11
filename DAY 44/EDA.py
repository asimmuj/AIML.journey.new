import pandas as pd
import matplotlib.pyplot as plt
data = {
    "student": ["Ali", "Sara", "Ahmed", "Zoya", "Mujtaba",
                "Aman", "Ayesha", "Rohan", "Fatima", "Kabir"],
    "study_hours": [2, 5, 3, 7, 4, 1, 6, 3, 8, 2],
    "attendance": [65, 90, 75, 95, 80, 50, 92, 70, 98, 60],
    "marks": [45, 82, 58, 94, 72, 35, 88, 55, 97, 42]
}
df = pd.DataFrame(data)
# 1. Inspect the dataset
print("First five rows:")
print(df.head())
print("\nDataset shape:")
print(df.shape)
print("\nDataset information:")
df.info()
# 2. Explore summary statistics
print("\nSummary statistics:")
print(df.describe())
print("\nAverage marks:")
print(df["marks"].mean())
print("\nMedian marks:")
print(df["marks"].median())
print("\nHighest marks:")
print(df["marks"].max())
# 3. Check data qualit
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
# 4. Explore the marks distribution
plt.hist(df["marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
# 5. Explore the relationship between study hours and marks
plt.scatter(df["study_hours"], df["marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
# 6. Explore correlations
print("\nCorrelation matrix:")
print(df[["study_hours", "attendance", "marks"]].corr())
# 7. Find the top three students
print("\nTop three students:")
print(df.sort_values("marks", ascending=False).head(3))
# 8. Compare average marks by study hours
print("\nAverage marks by study hours:")
print(df.groupby("study_hours")["marks"].mean())