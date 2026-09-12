def two_sum(numbers, target):
    left=0
    right=len(numbers)-1
    while left<right:
        sum=numbers[left]+numbers[right]
        if sum==target:
            print("pair found!")
            print(numbers[left],"+",numbers[right],"=",numbers[left]+numbers[right])
            print("indexes: ",left, right)
            break
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
    return -1
numbers = [1, 2, 4, 6, 8, 9]
target = 10
print("numbers: ",numbers)
print("target: ",target)
print("searching.....")
two_sum(numbers,target)