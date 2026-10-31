#exercise 1
numbers = [2, 4, 6, 8, 10]
mean = sum(numbers) / len(numbers)
total = 0
for number in numbers:
    difference = number - mean
    squared = difference ** 2
    total += squared
variance = total / len(numbers)
std_dev = variance ** 0.5
print("Numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

#exercise 2
marks = [10, 20, 30, 40, 50]
mean = sum(marks) / len(marks)
total = 0
for mark in marks:
    difference = mark - mean
    total += difference ** 2
variance = total / len(marks)
std_dev = variance ** 0.5
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)