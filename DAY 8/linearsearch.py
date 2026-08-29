def linear_search(numbers, target):
    for index, number in enumerate(numbers):
         if number == target:
            return index
    return -1
numbers = [10, 25, 7, 91, 43]
target = int(input("Enter number to search: "))
result = linear_search(numbers, target)
if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found.")