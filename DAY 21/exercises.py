# numbers = [1, 2, 3, 4, 6, 8]
# left=0
# right=len(numbers)-1
# while left<right:
#     sum=numbers[left]+numbers[right]
#     if sum==10:
#         print("found", left, right)
#         break
#     elif sum<10:
#         left=left+1
#     elif sum>10:
#         right=right-1

# #exercise 2
# numbers = [2, 3, 4, 7, 9, 12, 15]
# target = 16
# left=0
# right=len(numbers)-1
# while left<right:
#     sum=numbers[left]+numbers[right]
#     if sum==target:
#         print("found")
#         print("left index:", left)
#         print("right index:", right)
#         print(numbers[left], numbers[right])
#         break
#     elif sum<target:
#         left+=1
#     elif sum>target:
#         right-=1

#exercise 3
def two_sum(numbers, target):
    left=0
    right=len(numbers)-1
    while left<right:
        sum=numbers[left]+numbers[right]
        if sum==target:
            print("found", left, right)
            break
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
    return -1
numbers = [1, 2, 4, 6, 8, 9]
target = 10
two_sum(numbers,target)