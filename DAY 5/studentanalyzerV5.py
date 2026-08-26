enrollments = [
    ("Mujtaba", "Python"),
    ("Zeeshan", "Python"),
    ("Ali", "SQL"),
    ("Mujtaba", "SQL"),
    ("Sara", "Machine Learning"),
    ("Ali", "Python"),
    ("Zeeshan", "Machine Learning")
]
names=set()
courses=set()
for student in enrollments:
    names.add(student[0])
    courses.add(student[1])
print(names)
print(courses)
print(len(names))
print(len(courses))
python_students=set()
ml_students=set()
for student in enrollments:
    if student[1]=="Python":
        python_students.add(student[0])
    if student[1]=="Machine Learning":
        ml_students.add(student[0])
print(python_students)
print(ml_students)