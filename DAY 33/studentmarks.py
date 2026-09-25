import numpy as np
students = np.array([
    [18, 70, 80, 75],
    [19, 85, 90, 88],
    [18, 60, 72, 68],
    [20, 95, 91, 94],
    [19, 78, 84, 80]
])
# adding bonus marks
bonus = np.array([0, 5, 3, 2])
students = students + bonus
print("Updated student data:")
print(students)
# getting marks
marks = students[:, 1:]
# total marks
total = np.sum(marks, axis=1)
# average marks
average = np.mean(marks, axis=1)
print("\nTotal marks:")
print(total)
print("\nAverage marks:")
print(average)
print("\nHighest average:", np.max(average))
print("Lowest average:", np.min(average))