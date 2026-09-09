#exercise 1
# def countdown(n):
#     if n==0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)

#exercise 2
# def recursive_sum(n):
#     if n==1:
#         return 1
#     return n+recursive_sum(n-1)
# print(recursive_sum(5))

#exercise 3
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))