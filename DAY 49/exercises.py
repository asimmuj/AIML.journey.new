import numpy as np
A = np.array([
    [2, 4],
    [6, 8]
])
B = np.array([
    [1, 3],
    [5, 7]
])
result = A + B
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Addition:")
print(result)

#exercise 2
import numpy as np
A = np.array([
    [3, 6],
    [9, 12]
])
result = A * 3
print("Original matrix:")
print(A)
print("After multiplication:")
print(result)

#exercise 3
import numpy as np
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Original matrix:")
print(A)
print("Transpose:")
print(A.T)

#exercise 4
import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [2, 0],
    [1, 2]
])
result = A @ B
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix multiplication:")
print(result)

