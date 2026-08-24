# def greet(name):
#     print("Hello",name)
# greet("mujtaba")

# def checkeven(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# checkeven(10)
# checkeven(7)
# checkeven(24)
# checkeven(31)

# def findmax(a,b):
#     if a>b:
#         print(f"{a} is greatest")
#     else:
#         print(f"{b} is greatest")
# findmax(5,6)


def count_passed(marks):
    count=0
    for mark in marks:
        if mark>=40:
            count+=1
    print(count)
marks = [35, 78, 91, 42, 67, 29, 88]
count_passed(marks)