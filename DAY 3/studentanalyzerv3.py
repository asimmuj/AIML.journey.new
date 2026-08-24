marks = [35, 78, 91, 42, 67, 29, 88]

def total(marks):
    count=0
    for mark in marks:
        count+=1
    print("total students: ",count)
def count_passed(marks):
    count=0
    for mark in marks:
        if mark>=40:
            count+=1
    print("passed students: ",count)
def failed(marks):
    count=0
    for mark in marks:
        if mark<40:
            count+=1
    print("failed student: ",count)
def highest(marks):
    print("highest marks: ",max(marks))
def lowest(marks):
    print("lowest marks: ",min(marks))
def average(marks):
    avg = sum(marks)/len(marks)
    print("average of marks: ",avg)

total(marks)
count_passed(marks)
failed(marks)
highest(marks)
lowest(marks)
average(marks)