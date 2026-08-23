marks = [35, 78, 91, 42, 67, 29, 88]
count=0
for mark in marks:
        count+=1
print("total students: ", count)
passed=0
for mark in marks:
    if mark>=40:
        passed+=1
print("passed students: ",passed)
failed=0
for mark in marks:
     if mark<40:
        failed+=1
print("failed students: ",failed)
total=0
for mark in marks:
     total=total+mark
print("total marks: ",total)
average=total/count
print("average: ",average)
highest=marks[0]
for mark in marks:
     if mark>highest:
          highest=mark
print("highest: ",highest)
lowest=marks[0]
for mark in marks:
     if mark<lowest:
          lowest=mark
print("lowest: ", lowest)
