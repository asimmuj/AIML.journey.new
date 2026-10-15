import numpy as np
# Marks of a student in three subjects
marks = np.array([80, 75, 90])
# Target marks
target = np.array([85, 80, 95])
# Difference between target and current marks
difference = target - marks
# Total and average marks
total = np.sum(marks)
average = np.mean(marks)
# Length of the marks vector
length = np.linalg.norm(marks)
print("Marks:", marks)
print("Target:", target)
print("Difference:", difference)
print("Total:", total)
print("Average:", average)
print("Vector magnitude:", round(length, 2))