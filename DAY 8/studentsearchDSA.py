students = [
    "Mujtaba",
    "Zeeshan",
    "Ali",
    "Sara",
    "Ahmed"
]

name = input("Enter student name: ")

found = False

for index, student in enumerate(students):
    if student == name:
        print("Student found at position", index)
        found = True
        break

if not found:
    print("Student not found.")