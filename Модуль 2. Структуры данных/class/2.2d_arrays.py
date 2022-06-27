# 2d example
arr = [[1, 2, 3], [4, 5, 6], [8, 8, 9]]
# print(arr[0])
# print(arr[0][2])
# for item in arr:
#     print(item)
# for item in arr:
#     for element in item:
#         print(element, end=" ")
#     print()
################################################################
# Find the sum of the elements of the array
# def arr_sum_2d(arr):
#     result = 0
#     for item in arr:
#         for element in item:
#             result += element
#             print(element)
#     return result


# print(arr_sum_2d(arr))
################################################################
# Find all even elements in the 2d array
# def get_even_2d(arr):
#     result = []
#     for item in arr:
#         for element in item:
#             if element % 2 == 0:
#                 result.append(element)
#     return result


# print(get_even_2d(arr))
################################################################
# Find the sum of elements on the main diagonal
# def get_diagonal_sum_2d(arr):
#     result = 0
#     for i in range(len(arr)):
#         result += arr[i][i]
#     return result
# def get_diagonal_sum_2d(arr):
#     result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i == j:
#                 result += arr[i][j]
#     return result


# print(get_diagonal_sum_2d(arr))
################################################################
# Find the sum of elements on the secondary diagonal
# def get_secondary_diagonal_sum_2d(arr):
#     result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i + j == len(arr) - 1:
#                 result += arr[i][j]
#     return result
# def get_secondary_diagonal_sum_2d(arr):
#     result = 0
#     for i in range(len(arr)):
#         result += arr[i][len(arr) - i - 1]
#     return result

# print(get_secondary_diagonal_sum_2d(arr))
################################################################
# Find the max element of the 2d array at each row
# def get_max(arr):
#     max_elem = arr[0]
#     for item in arr:
#         if item > max_elem:
#             max_elem = item
#     return max_elem


# def get_max_row_2d(arr):
#     result = []
#     for item in arr:
#         result.append(get_max(item))
#     return result


# print(get_max_row_2d(arr))
