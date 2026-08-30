#linear search
def linearsearch(students, target):
    found=False
    for i in range(len(students)):
        if students[i]==target:
            found=True
            print("student found!")
            print("index: ",i)
            break
    if found==False:
        print("student not found!")
students = [
    "Mujtaba",
    "Zeeshan",
    "Ali",
    "Sara",
    "Ahmed"
]
target=input("enter student name: ")
linearsearch(students, target)