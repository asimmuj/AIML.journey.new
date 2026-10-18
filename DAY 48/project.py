
import numpy as np

# Marks of 4 students in 3 subjects
marks = np.array([
    [80, 75, 90],
    [85, 92, 88],
    [70, 78, 82],
    [65, 80, 72]
])

print("Student Marks:")
print(marks)

print("\nMatrix Shape:", marks.shape)
print("Number of Dimensions:", marks.ndim)

# Marks of the second student
print("\nMarks of Second Student:")
print(marks[1])

# Computer Science marks of all students
print("\nComputer Science Marks:")
print(marks[:, 2])
