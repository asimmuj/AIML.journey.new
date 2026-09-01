# def binarsearch(numbers,target):
#     low = 0
#     high = len(numbers)-1
#     while low<=high:
#         mid= (low+high)//2
#         if numbers[mid]==target:
#             return mid
#         elif target>numbers[mid]:
#             low = mid+1
#         else:
#             high=mid-1
#     return -1
# numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72]
# target=int(input("enter a number to search: "))
# index=binarsearch(numbers,target)
# print("index: ",index)

#if we search for 23 it gives index as 5
#if we search for 25 it gives index as -1 because it doesn't exists.