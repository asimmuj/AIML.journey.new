import numpy as np
A = np.array([
    [2, 4, 6],
    [1, 3, 5]
])
print("Matrix:")
print(A)
print("Shape:", A.shape)

#exercise 2
import numpy as np
A = np.array([
    [5, 8],
    [3, 9]
])
print(A[1, 0])

#exercise 3
import numpy as np

marks = np.array([
    [80, 75, 90],
    [85, 92, 88],
    [70, 78, 82],
    [65, 80, 72]
])

print(marks)
print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)

#exercise 4
A = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Number of rows:", len(A))
print("Number of columns:", len(A[0]))