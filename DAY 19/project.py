def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

def product_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)

def reverse_number(n, reversed_num=0):
    n = abs(n)
    if n == 0:
        return reversed_num
    return reverse_number(n // 10, reversed_num * 10 + n % 10)

def palindrome(n):
    n = abs(n)
    return n == reverse_number(n)

# Main program
number = int(input("Enter a number: "))

print("Number of digits:", count_digits(number))
print("Sum of digits:", sum_digits(number))
print("Product of digits:", product_digits(number))
print("Reverse:", reverse_number(number))
print("Palindrome:", palindrome(number))