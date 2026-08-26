# data=("mujtaba",18,"CSE",7.2)
# name,age,branch,cgpa=data
# print(name)
# print(age)
# print(branch)
# print(cgpa)

# numbers = {10, 20, 20, 30, 30, 30, 40}
# print(numbers)

# python = {"Ali", "Mujtaba", "Zeeshan", "Ahmed"}
# sql = {"Mujtaba", "Ahmed", "Sara"}
# print("student who know python or sql: ",python|sql)
# print("students who know both: ",python&sql)
# print("students who know python but not sql: ",python-sql)

students = [
    ("Mujtaba", "CSE"),
    ("Zeeshan", "CSE"),
    ("Ali", "ECE"),
    ("Mujtaba", "CSE"),
    ("Sara", "AI")
]

names = set()
branches = set()

for student in students:
    names.add(student[0])
    branches.add(student[1])

print(names)
print(branches)