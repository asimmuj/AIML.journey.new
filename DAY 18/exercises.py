# def countdown(n):
#     if n==0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)

# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# print(sum(10))

def power(a,n):
    if n==1:
        return a
    return a*power(a,n-1)
print(power(2,5))