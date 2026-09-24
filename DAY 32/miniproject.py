#student marks analyzer
import numpy as np
students = np.array([
    [18, 85, 78, 80],
    [19, 90, 88, 92],
    [18, 72, 75, 70],
    [20, 95, 91, 94],
    [19, 82, 79, 85]
])
print("Student Data:")
print(students)
print("\nAges:")
print(students[:, 0])
print("\nMath Marks:")
print(students[:, 1])
print("\nPython Marks:")
print(students[:, 2])
print("\nML Marks:")
print(students[:, 3])
print("\nFirst 3 Students:")
print(students[:3])
print("\nLast 2 Students:")
print(students[-2:])
print("\nMath and Python Marks:")
print(students[:, 1:3])
highest_math = students[:, 1].max()
print("\nHighest Math Mark:", highest_math)
student = students[students[:, 1] == highest_math]
print("Student with highest Math mark:")
print(student)