# import numpy as np
# numbers = np.array([15, 25, 35, 45, 55, 65])
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])
# print(numbers[-2])

# #exercise 2
# import numpy as np
# marks = np.array([
#     [78, 85, 90],
#     [65, 72, 80],
#     [88, 91, 95],
#     [55, 60, 70]
# ])
# print("1st student marks", marks[0])
# print("3rd student's 2nd subject marks", marks[2,1])
# print("last student's last subject marks", marks[-1,-1])
# print("second row", marks[1])

# #exercise 3
# import numpy as np
# numbers = np.arange(1, 21)
# print(numbers[0:5])
# print(numbers[-5:])
# print(numbers[5:15])
# print(numbers[::2])
# print(numbers[::-1])

#exercise 4
import numpy as np
students = np.array([
    [18, 85, 72],
    [19, 90, 88],
    [18, 76, 80],
    [20, 95, 91],
    [19, 82, 79]
])
print("ages: ",students[:,0])
print("math marks: ",students[:,1])
print("python marks: ",students[:,2])
print("maths and python marks:", students[:,-2:])
print("first 3 students: ",students[0:3])