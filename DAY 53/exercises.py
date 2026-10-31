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

#exercise 3
A = [40, 45, 50, 55, 60]
B = [10, 30, 50, 70, 90]
mean_A = sum(A) / len(A)
mean_B = sum(B) / len(B)
total_A = 0
total_B = 0
for number in A:
    total_A += (number - mean_A) ** 2
for number in B:
    total_B += (number - mean_B) ** 2
variance_A = total_A / len(A)
variance_B = total_B / len(B)
std_A = variance_A ** 0.5
std_B = variance_B ** 0.5
print("Dataset A")
print("Mean:", mean_A)
print("Variance:", variance_A)
print("Standard Deviation:", std_A)
print("\nDataset B")
print("Mean:", mean_B)
print("Variance:", variance_B)
print("Standard Deviation:", std_B)
if variance_A < variance_B:
    print("\nDataset A is more consistent.")
else:
    print("\nDataset B is more consistent.")

#exercise 4
numbers = []
for i in range(5):
    number = float(input("Enter a number: "))
    numbers.append(number)
mean = sum(numbers) / len(numbers)
total = 0
for number in numbers:
    difference = number - mean
    total += difference ** 2
variance = total / len(numbers)
std_dev = variance ** 0.5
print("\nResults")
print("Numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)