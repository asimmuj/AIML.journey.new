#exercise 1
numbers = [1, 2, 2, 3, 1, 4, 2, 3, 5]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("Frequency:", frequency)