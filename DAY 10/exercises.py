def binarysearch(numbers, target):
    low =0
    high= len(numbers)-1
    while low<=high:
        mid=(low+high)//2
        if target==numbers[mid]:
            return mid
        elif target>numbers[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
numbers = [5, 12, 18, 23, 31, 42, 57, 64, 78, 91]
target=int(input("enter a number to search: "))
print(binarysearch(numbers,target))
#commit