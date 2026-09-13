marks = [65, 72, 81, 55, 90, 88, 76, 95, 84]
k=int(input("enter window size: "))
window_sum = sum(marks[:k])
maximum = window_sum
for right in range(k, len(marks)):
    window_sum = window_sum - marks[right - k]
    window_sum = window_sum + marks[right]
    if window_sum < maximum:
        maximum = window_sum

minimum = window_sum
for right in range(k, len(marks)):
    window_sum = window_sum - marks[right - k]
    window_sum = window_sum + marks[right]
    if window_sum < minimum:
        minimum = window_sum
print(maximum//k)
print(minimum//k)
print(maximum)
print(minimum)