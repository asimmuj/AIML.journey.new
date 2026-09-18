students = [
    "adnan",
    "maliha",
    "adnan",
    "zeeshan",
    "maliha",
    "Mujtaba",
    "adnan"
]
# Count attendance
attendance = {}
for student in students:
    if student in attendance:
        attendance[student] += 1
    else:
        attendance[student] = 1
print("Attendance:")
for student in attendance:
    print(student, "→", attendance[student])
# Find most present student
most_present = None
highest_attendance = 0
for student in attendance:
    if attendance[student] > highest_attendance:
        highest_attendance = attendance[student]
        most_present = student
print("\nMost present:", most_present)
print("Attendance:", highest_attendance)
# Find students appearing only once
print("\nStudents appearing only once:")
for student in attendance:
    if attendance[student] == 1:
        print(student)
# Find total unique students
unique_students = set(students)
print("\nUnique students:", len(unique_students))