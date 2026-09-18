students = {
    "Mujtaba": 85,
    "Ali": 72,
    "Sara": 91,
    "Ahmed": 85,
    "Zeeshan": 72
}
# 1. Print all students and marks
for name, marks in students.items():
    print(name, ":", marks)
# 2. Find highest marks
highest = max(students.values())
print("\nHighest marks:", highest)
print("Student(s) with highest marks:")
for name, marks in students.items():
    if marks == highest:
        print(name)
# 3. Find lowest marks
lowest = min(students.values())
print("\nLowest marks:", lowest)
print("Student(s) with lowest marks:")
for name, marks in students.items():
    if marks == lowest:
        print(name)
# 4. Count frequency of each score
marks_frequency = {}
for marks in students.values():
    if marks in marks_frequency:
        marks_frequency[marks] += 1
    else:
        marks_frequency[marks] = 1

for marks, count in marks_frequency.items():
    print(marks, "→", count)
# 5. Search for a student
search_name = input("\nEnter student name: ")
if search_name in students:
    print("Student found!")
    print("Marks:", students[search_name])
else:
    print("Student not found")