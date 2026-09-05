# numbers=[8, 4, 6, 2, 7]
# def insertionsort(numbers):
#     for i in range(1,len(numbers)):
#         key=numbers[i]
#         j=i-1
#         while j>=0 and numbers[j]>key:
#             numbers[j+1]=numbers[j]
#             j-=1
#             numbers[j+1]=key
#     return numbers
# print(insertionsort(numbers))

numbers=[8, 4, 6, 2, 7]
def insertionsort(numbers):
    for i in range(1,len(numbers)):
        key=numbers[i]
        j=i-1
        while j>=0 and numbers[j]<key:
            numbers[j+1]=numbers[j]
            j-=1
            numbers[j+1]=key
    return numbers
print(insertionsort(numbers))