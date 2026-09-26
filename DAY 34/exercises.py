# import numpy as np
# marks = np.array([78, 85, 92, 67, 88])
# print(marks.sum())
# print(marks.mean())
# a=marks.max()
# b=marks.min()
# print(a)
# print(b)
# print(a-b)

# #exercise 2
# import numpy as np
# salary = np.array([25000, 30000, 28000, 35000, 40000])
# print(salary+5000)
# print(salary.mean())
# print(salary.max())
# print(salary.min())

#exercise 3
import numpy as np
marks = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [92, 95, 89],
    [70, 78, 85]
])
print(np.sum(marks, axis=1))
print(np.mean(marks, axis=1))
print(np.sum(marks, axis=0))
print(np.mean(marks, axis=0))
print(marks.max())