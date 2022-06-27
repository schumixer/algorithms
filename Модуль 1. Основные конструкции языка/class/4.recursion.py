# def f(n):
#     if n > 0:
#         print(n)
#         f(n - 1)
# def f(n):
#     if n > 0:
#         f(n - 1)
#         print(n)
# def f(n):
#     if n > 0:
#         print(n)
#         f(n - 1)
#         print(n)

# f(3)
######################################
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(4))
