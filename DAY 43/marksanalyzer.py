import numpy as np
import matplotlib.pyplot as plt

marks = [45, 48, 52, 55, 58, 60, 62, 65, 70, 95]

# Calculate statistics
average = np.mean(marks)
median = np.median(marks)
highest = np.max(marks)
lowest = np.min(marks)
std_dev = np.std(marks)

print("Student Performance Report")
print("Average marks:", round(average, 2))
print("Median marks:", median)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Standard deviation:", round(std_dev, 2))

# Create three graphs
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.subplot(1, 3, 2)
plt.boxplot(marks)
plt.title("Marks Spread")
plt.ylabel("Marks")

plt.subplot(1, 3, 3)
students = list(range(1, len(marks) + 1))
plt.scatter(students, marks)
plt.title("Marks by Student")
plt.xlabel("Student Number")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()