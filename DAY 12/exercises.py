#tracing mid values
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target = 35

def binarysearch(numbers,target):
    low=0
    high=0
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return numbers[mid]
        elif target>numbers[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binarysearch(numbers,target))