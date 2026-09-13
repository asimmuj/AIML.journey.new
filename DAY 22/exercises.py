# numbers = [4, 2, 1, 7, 8, 1, 2]
# k = 3

# window_sum = sum(numbers[:k])
# maximum = window_sum
# for right in range(k, len(numbers)):
#     window_sum = window_sum - numbers[right - k]
#     window_sum = window_sum + numbers[right]
#     if window_sum > maximum:
#         maximum = window_sum
# print(maximum)

#exercise 2
# numbers = [2, 4, 6, 8, 10, 12]
# k = 3
# window_sum = sum(numbers[:k])
# maximum = window_sum

# for right in range(k, len(numbers)):
#     window_sum = window_sum - numbers[right - k]
#     window_sum = window_sum + numbers[right]

#     if window_sum > maximum:
#         maximum = window_sum

# print(maximum / k)

#exercise 3
numbers = [5, 2, 8, 1, 3, 4]
k = 2
window_sum = sum(numbers[:k])
minimum = window_sum

for right in range(k, len(numbers)):
    window_sum = window_sum - numbers[right - k]
    window_sum = window_sum + numbers[right]

    if window_sum < minimum:
        minimum = window_sum

print(minimum)