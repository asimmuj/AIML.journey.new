# #exesrcise 1
# def count_positive(numbers):
#     count=0
#     for number in numbers:
#         if number>=0:
#             count+=1
#     return count
# numbers=[-5, 3, 7, -2, 0, 8]
# print(count_positive(numbers))

#exercise 2
# def find_largest(numbers):
#     largest=numbers[0]
#     for number in numbers:
#         if number>largest:
#             largest=number
#     return largest
# numbers=[-5, 3, 7, -2, 0, 8]
# print(find_largest(numbers))

#exercise 3
numbers = [4, 7, 2, 7, 9, 4, 7, 1]
largest=numbers[0]
smallest=numbers[0]
counteven=0
countodd=0
total=0

for number in numbers:
    if number>largest:
        largest=number
    if number<smallest:
        smallest=number
    if number%2==0:
        counteven+=1
    if number%2!=0:
        countodd+=1
    total+=number
    average=total/len(numbers)
print("largest: ",largest)
print("smallest:",smallest)
print("no of even:",counteven)
print("no of odd:",countodd)
print("total: ",total)
print("average: ",average)