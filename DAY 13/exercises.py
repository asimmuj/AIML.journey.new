numbers = [10, 20, 20, 20, 30, 40, 50]
def first_occurrence(numbers, target):
    low = 0
    high = len(numbers) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            result = mid
            # Search further left
            high = mid - 1
        elif target > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return result

numbers = [10, 20, 20, 20, 30, 40, 50]
target = int(input("Enter number: "))
result = first_occurrence(numbers, target)
if result != -1:
    print("First occurrence:", result)
else:
    print("Number not found!")...