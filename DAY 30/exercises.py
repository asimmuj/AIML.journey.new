numbers = [3, 5, 3, 8, 5, 3, 9, 8, 5]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("Frequency:")
for number, count in frequency.items():
    print(number, "-", count)