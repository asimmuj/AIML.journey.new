marks = [78, 45, 92, 33, 67, 88, 51, 29, 95, 61]
total =0
largest=marks[0]
smallest=marks[0]
countpassed=0
countfailed=0
counteven=0
countodd=0
for mark in marks:
    if mark>largest:
        mark=largest
    if mark<smallest:
        mark=smallest
    total+=mark
    avg=total/len(marks)
    if mark%2==0:
        counteven+=1
    if mark%2!=0:
        countodd+=1
    if mark>40:
        countpassed+=1
    if mark<=40:
        countfailed+=1
print(total)
print(largest)
print(smallest)
print(avg)
print(countpassed)
print(countfailed)
print(counteven)
print(countodd)
