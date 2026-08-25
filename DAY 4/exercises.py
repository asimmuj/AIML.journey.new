# student={
#     "name":"mujtaba",
#     "age":22,
#     "marks":85,
#     "college":"MJCET"
# }
# print(student["name"], student["marks"])
# student["city"]="HYD"
# student["marks"]=90
# for key in student:
#     if "email" in student:
#         print(student["email"])
#     else:
#         print("no email")
# for key, value in student.items():
#     print(key, ":", value)

# marks = {
#     "Python": 85,
#     "Math": 35,
#     "SQL": 90,
#     "English": 72,
#     "Physics": 28
# }

# total = 0
# count_passed = 0
# count_failed = 0
# maximum = 0
# minimum = 100

# for subject, mark in marks.items():

#     total += mark

#     if mark >= 40:
#         count_passed += 1
#     else:
#         count_failed += 1

#     if mark > maximum:
#         maximum = mark

#     if mark < minimum:
#         minimum = mark

# average = total / len(marks)

# print("Total:", total)
# print("Average:", average)
# print("Passed:", count_passed)
# print("Failed:", count_failed)
# print("Highest:", maximum)
# print("Lowest:", minimum)

def analyze_student(marks):
    total=0
    for subject, mark in marks.items():
        total+=mark
    average=total/len(marks)
    return average
marks={
    "Python": 85,
    "Math": 78,
    "SQL": 90
}
print("average: ",analyze_student(marks))