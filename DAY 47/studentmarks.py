import numpy as np
# Marks in five subjects
marks = np.array([80, 75, 90, 68, 85])
# Target marks for each subject
target = np.array([85, 80, 95, 75, 90])
# Weights for each subject
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
# Calculate total and average
total = np.sum(marks)
average = np.mean(marks)
# Find highest and lowest marks
highest = np.max(marks)
lowest = np.min(marks)
# Find the difference between target and actual marks
difference = target - marks
# Calculate weighted score using dot product
weighted_score = np.dot(marks, weights)
print("Subject marks:", marks)
print("Total marks:", total)
print("Average marks:", round(average, 2))
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("\nTarget marks:", target)
print("Marks needed:", difference)
print("\nWeighted score:", round(weighted_score, 2))