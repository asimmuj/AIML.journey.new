# def find_number(numbers,target):
#     for number in numbers:
#         if number==target:
#             return True
#     return False
# numbers=[10,20,30,40,50]
# result=find_number(numbers,60)
# print(result)

# def count_occurances(numbers,target):
#     count=0
#     for number in numbers:
#         if number==target:
#             count+=1
#     return count
# numbers=[10,40,40,40,50]
# result=count_occurances(numbers,40)
# print(result)

def find_max(numbers):
    return max(numbers)
result=find_max([10,20,30,40,50])
print(result)