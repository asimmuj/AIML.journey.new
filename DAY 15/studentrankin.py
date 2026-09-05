students = [
    ["Ali", 78],
    ["Sara", 92],
    ["Zeeshan", 85],
    ["Mujtaba", 95],
    ["Ahmed", 68]
]
def insertionsort(students):
    for i in range(1,len(students)):
        key=students[i][1]
        j=i-1
        while j>=0 and students[j][1]<key:
            students[j+1][1]=students[j][1]
            j-=1
            students[j+1][1]=key
    return students
print(insertionsort(students))

