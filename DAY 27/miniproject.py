def constant_example(numbers):
    print("First element:", numbers[0])
def linear_example(numbers):
    for number in numbers:
        print(number)
def quadratic_example(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)
def binary_search_example(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
numbers = [10, 20, 30, 40, 50]
print("O(1) Example ")
constant_example(numbers)
print("\nO(n) Example ")
linear_example(numbers)
print("\nO(n²) Example ")
quadratic_example(numbers)
print("\nO(log n) Example")
target = 40
result = binary_search_example(numbers, target)
if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found")