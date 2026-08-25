students = {
    "Mujtaba": [78, 85, 91],
    "Zeeshan": [65, 72, 80],
    "Ahmed": [35, 42, 38],
    "Sofia": [90, 95, 88]
}


def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average


for name, marks in students.items():

    average = calculate_average(marks)

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print("Student:", name)
    print("Average:", round(average, 2))
    print("Status:", status)
    print()