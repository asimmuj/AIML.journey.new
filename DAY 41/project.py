import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Ahmed", "Mujtaba", "Zeeshan"]

python_marks = [78, 92, 85, 88, 74]
math_marks = [82, 89, 79, 91, 70]

# Highest marks
python_highest = max(python_marks)
math_highest = max(math_marks)

print("Highest Python marks:", python_highest)
print("Highest Math marks:", math_highest)

# Python marks
plt.bar(students, python_marks)
plt.xlabel("Students")
plt.ylabel("Python Marks")
plt.title("Python Marks")
plt.show()

# Math marks
plt.bar(students, math_marks)
plt.xlabel("Students")
plt.ylabel("Math Marks")
plt.title("Math Marks")
plt.show()

# Python vs Math
plt.scatter(python_marks, math_marks)
plt.xlabel("Python Marks")
plt.ylabel("Math Marks")
plt.title("Python Marks vs Math Marks")
plt.show()