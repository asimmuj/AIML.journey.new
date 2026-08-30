# def linearsearch(numbers,target):
#     for i in range(len(numbers)):
#         if numbers[i]==target:
#             return i
#     return -1
# numbers = [5, 10, 15, 20, 25]
# target=int(input("enter target: "))
# index=linearsearch(numbers, target)
# print(index)

def linearsearch(numbers,target):
    for i in range(len(numbers)):
        if numbers[i]==target:
            return i
        break
    return -1
numbers = [12, 7, 19, 7, 25, 7]
target=int(input("enter target: "))
index=linearsearch(numbers, target)
print(index)