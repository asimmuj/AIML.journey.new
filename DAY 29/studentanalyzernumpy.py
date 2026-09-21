import numpy as np
# Student marks
marks = np.array([
    78,
    85,
    92,
    67,
    88,
    74,
    95,
    61,
    83,
    90
])
# Calculations
number_of_students = marks.size
average_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
total_marks = np.sum(marks)
# Boolean masking
above_80 = marks[marks > 80]
below_70 = marks[marks < 70]
# Pass percentage
passed_students = marks[marks >= 40]
pass_percentage = (passed_students.size / number_of_students) * 100
# Display results
print("Number of students:", number_of_students)
print("Average marks:", average_marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Total marks:", total_marks)
print("Students scoring above 80:", above_80)
print("Number scoring above 80:", above_80.size)
print("Students scoring below 70:", below_70)
print("Number scoring below 70:", below_70.size)
print("Pass percentage:", pass_percentage, "%")