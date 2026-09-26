import numpy as np
students = np.array([
    [78, 85, 90],
    [65, 70, 72],
    [88, 92, 95],
    [55, 68, 60],
    [90, 86, 89]
])
print("student wise total:", np.sum(students,axis=1))
print("student wise average:", np.mean(students,axis=1))
print("subject wise total:", np.sum(students,axis=0))
print("subject wise average:", np.mean(students,axis=0))
print("overall average:", students.mean())
print("highest marks: ",students.max())
print("lowest marks: ",students.min())