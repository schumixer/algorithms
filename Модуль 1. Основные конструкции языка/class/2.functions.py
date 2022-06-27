# number = int(input("enter number: "))
# is_simple = True
# for i in range(2, number):
#     if number % i == 0:
#         is_simple = False
#         break
# print(number, is_simple)
########################################################################
# def is_simple_checker(number):
#     is_simple = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#     print(number, is_simple)


# left = int(input("enter left bound: "))
# right = int(input("enter right bound: "))
# for number in range(left, right + 1):
#     is_simple_checker(number)

# is_simple_checker(203)
######################################################################
# def f(x, y):
#     z = x + y
#     return z


# x = f(3, 4) * f(7, 8)
# print(x)
################################################################
def smth():
    pass


def factorial(num):
    res = 1
    for i in range(2, num + 1):
        res = res * i
    # smth()
    return res


x = factorial(5)
y = factorial(4)
z = x + y
print(z)
