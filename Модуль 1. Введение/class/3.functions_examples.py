# n = 3
# *
# **
# ***
# def triangle_left(n):
#     symbol = "*"
#     for i in range(n):
#         print(symbol * (i + 1))
# def triangle_left(n):
#     symbol = "*"
#     for row_number in range(1, n + 1, 1):
#         string = ""
#         for i in range(1, row_number + 1):
#             string += symbol
#         print(string)
################################################################
# n = 3
# --*
# -**
# ***
def triangle_left(n):
    symbol = "*"
    space = "-"
    for row_number in range(1, n + 1, 1):
        string_star = ""
        string_space = ""
        for i in range(n - row_number, 0, -1):
            string_space += space
        for i in range(1, row_number + 1):
            string_star += symbol
        print(string_space, end="")
        print(string_star)


n = int(input("Enter the number of rows: "))
triangle_left(n)
