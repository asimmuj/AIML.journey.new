#exercise 1: calculation
'''a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("multiplication",(a*b))
print("addition",(a+b))
print("subtraction",(a-b))
print("division",(a/b))'''


#exercise 2: even or odd
'''num=int(input("enter a number"))
if num%2==0:
    print("given number is even")
else:
    print("number is odd")'''


#exrecise 3: greatest of 3 numbers
'''a=int(input("enter 1st nummber"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
else:
    print("c is greatest")'''


#exercise 4: average of list
'''marks = [78, 85, 91, 66, 73]
avg=sum(marks)/len(marks)
print(avg)'''


#exercise 5: counting number of student scoring atleast 40.
'''marks = [35, 78, 91, 42, 67, 29, 88]
count=0
for i in marks:
    if i>=40:
        count +=1
        print(count)'''