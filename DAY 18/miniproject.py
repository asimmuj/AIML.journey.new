def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + (n % 10))

number = int(input("Enter a positive integer: "))
print("Number of digits:", count_digits(number))
print("Sum of digits:", sum_digits(number))