'''a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("multiplication",(a*b))
print("addition",(a+b))
print("subtraction",(a-b))
print("division",(a/b))'''

'''num=int(input("enter a number"))
if num%2==0:
    print("given number is even")
else:
    print("number is odd")'''

'''a=int(input("enter 1st nummber"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a>b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
else:
    print("c is greatest")'''

'''marks = [78, 85, 91, 66, 73]
avg=sum(marks)/len(marks)
print(avg)'''

marks = [35, 78, 91, 42, 67, 29, 88]
count=0
for i in marks:
    if i>=40:
        count +=1
        print(count)