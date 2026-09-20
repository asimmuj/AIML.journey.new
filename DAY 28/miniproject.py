students = {
    "Ali": 78,
    "Ahmed": 92,
    "Sara": 85,
    "Mujtaba": 67,
    "Zeeshan": 92,
    "Ayesha": 74
}
def display_students(students):
    print("\nStudent Marks:")
    for name, marks in students.items():
        print(name, ":", marks)
def calculate_average(students):
    total = sum(students.values())
    average = total / len(students)
    return average
def find_highest(students):
    highest_name = None
    highest_marks = -1
    for name, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            highest_name = name
    return highest_name, highest_marks
def find_lowest(students):
    lowest_name = None
    lowest_marks = float("inf")
    for name, marks in students.items():
        if marks < lowest_marks:
            lowest_marks = marks
            lowest_name = name
    return lowest_name, lowest_marks
def search_student(students, target):
    if target in students:
        return students[target]
    return None
def sort_students(students):
    return sorted(
        students.items(),
        key=lambda item: item[1],
        reverse=True
    )
def above_average(students, average):
    result = {}
    for name, marks in students.items():
        if marks > average:
            result[name] = marks
    return result
# Display students
display_students(students)
# Average
average = calculate_average(students)
print("\nAverage:", average)
# Highest
highest_name, highest_marks = find_highest(students)
print("\nHighest:", highest_name, "-", highest_marks)
# Lowest
lowest_name, lowest_marks = find_lowest(students)
print("Lowest:", lowest_name, "-", lowest_marks)
# Search
target = input("\nEnter student name to search: ")
marks = search_student(students, target)
if marks is not None:
    print(target, "scored", marks)
else:
    print("Student not found")
# Sorted students
print("\nStudents sorted by marks:")
sorted_students = sort_students(students)
for name, marks in sorted_students:
    print(name, ":", marks)
# Above average
print("\nStudents above average:")
result = above_average(students, average)
for name, marks in result.items():
    print(name, ":", marks)