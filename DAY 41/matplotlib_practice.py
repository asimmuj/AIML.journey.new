import matplotlib.pyplot as plt

students = [1, 2, 3, 4, 5]
marks = [65, 72, 81, 90, 76]

plt.bar(students, marks)

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()