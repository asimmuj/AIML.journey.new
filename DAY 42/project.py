
import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Ahmed", "Zeeshan", "Mujtaba"]

python_marks = [78, 92, 85, 70, 88]
math_marks = [82, 89, 76, 75, 90]

# 1. Compare Python marks of students
plt.bar(students, python_marks)

plt.title("Python Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# 2. Compare Python and Math marks
plt.scatter(python_marks, math_marks)

plt.title("Python Marks vs Math Marks")
plt.xlabel("Python Marks")
plt.ylabel("Math Marks")
plt.grid(True)

plt.show()

# 3. Check the distribution of Python marks
plt.hist(python_marks, bins=5, edgecolor="black")

plt.title("Distribution of Python Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# Find the highest and lowest Python marks
highest = max(python_marks)
lowest = min(python_marks)

high_index = python_marks.index(highest)
low_index = python_marks.index(lowest)

print("Highest Python marks:", students[high_index], "-", highest)
print("Lowest Python marks:", students[low_index], "-", lowest)