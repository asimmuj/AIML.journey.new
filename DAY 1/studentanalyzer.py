Name=str(input("Enter name of the student: "))
n=int(input("enter number of subjects: "))
marks=[]
for i in range (0,n):
    mark=float(input(f"enter marks of subject {i+1}: "))
    marks.append(mark)
total=sum(marks)
print("total: ",total)
average=total/len(marks)
print("average: ",average)
highest=max(marks)
print("highest: ",highest)
lowest=min(marks)
print("lowest: ",lowest)
if average>=40:
    status=print("passed")
else:
    status=print("failed")
if average<40:
    performance=print("fail")
elif average in (40,60):
    performance=print("needs improvement")
elif average in (60,75):
    performance=print("average")
elif average in (75,90):
    performance=print("good")
else:
    performance=print("excellent")