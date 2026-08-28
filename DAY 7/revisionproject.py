students = {
    "Mujtaba": [78, 85, 91],
    "Zeeshan": [65, 72, 80],
    "Ali": [90, 88, 95],
    "Sara": [55, 60, 58]
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