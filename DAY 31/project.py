#project
import numpy as np
data = np.array([
    [80, 75, 60, 85],
    [90, 88, 72, 91],
    [70, 65, 80, 78],
    [95, 92, 89, 94]
])
print("Student marks:")
print(data)
print("\nNumber of dimensions:", data.ndim)
print("Dataset shape:", data.shape)
print("Total values:", data.size)
print("Number of students:", data.shape[0])
print("Number of subjects:", data.shape[1])