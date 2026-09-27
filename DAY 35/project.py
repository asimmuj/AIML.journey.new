import pandas as pd

students = pd.DataFrame({
    "name": ["Mujtaba", "Ali", "Sara", "Ahmed", "Zeeshan",
             "Ayesha", "Hamza", "Fatima", "Usman", "Hina"],
    "age": [20, 19, 20, 18, 19, 20, 18, 19, 20, 18],
    "Python": [85, 72, 91, 68, 78, 88, 35, 74, 95, 62],
    "Math": [80, 75, 89, 70, 82, 91, 40, 68, 90, 65],
    "ML": [82, 70, 94, 65, 76, 85, 38, 72, 92, 60]
})

print("Student Data:")
print(students)

print("\nAverage Python marks:")
print(students["Python"].mean())

print("\nAverage Math marks:")
print(students["Math"].mean())

print("\nAverage ML marks:")
print(students["ML"].mean())

print("\nHighest Python mark:")
print(students["Python"].max())

print("\nHighest ML mark:")
print(students["ML"].max())

print("\nLowest Python mark:")
print(students["Python"].min())

# Total marks
students["total"] = students["Python"] + students["Math"] + students["ML"]

# Average marks
students["average"] = students["total"] / 3
print("\nFinal Student Report:")
print(students)