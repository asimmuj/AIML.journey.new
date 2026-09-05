# def bubblesort(numbers):
#     n = len(numbers)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if numbers[j] > numbers[j + 1]:
#              numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     return numbers
# numbers = [5, 1, 4, 2, 8]
# print(bubblesort(numbers))

def bubblesort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] <  numbers[j + 1]:
             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
numbers = [5, 1, 4, 2, 8]
print(bubblesort(numbers))