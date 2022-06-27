arr = [10, 20, 301, 40, 50]
# print(arr[0], arr[1], arr[10])
# i = 0
# while i < len(arr):
#     print(arr[i])
#     i += 1
# for i in range(0, len(arr), 1):
#     print(arr[i])
# for item in arr:
#     print(item)
########################################################################
# Find the sum of all the numbers in the list
# def get_sum(arr):
#     result = 0
#     for item in arr:
#         result += item
#     return result


# print(get_sum(arr))
########################################################################
# Find the max number in the list
# def get_max(arr):
#     max_elem = arr[0]
#     for item in arr:
#         if item > max_elem:
#             max_elem = item
#     return max_elem


# print(get_max(arr))
########################################################################

# Find the min number in the list
# def get_min(arr):
#     min_elem = arr[0]
#     for item in arr:
#         if item < min_elem:
#             min_elem = item
#     return min_elem


# print(get_min(arr))
########################################################################
# Find the index of the max number in the list
# def get_max_index(arr):
#     max_elem = arr[0]
#     max_index = 0
#     i = 0
#     for item in arr:
#         if item > max_elem:
#             max_elem = item
#             max_index = i
#         i += 1
#     return max_index


# print(get_max_index(arr))
########################################################################
# Reverse the list
# def reverse(arr):
#     return arr[::-1]
# def reverse(arr):
#     for i in range(len(arr) // 2):
#         temp = arr[i]
#         arr[i] = arr[len(arr) - 1 - i]
#         arr[len(arr) - 1 - i] = temp
#     return arr
# def reverse(arr):
#     result = []
#     for i in range(len(arr) - 1, -1, -1):
#         result.append(arr[i])
#     return result


# print(reverse(arr))
########################################################################
# Find all even numbers in the list
# def get_even(arr):
#     result = []
#     for item in arr:
#         if item % 2 == 0:
#             result.append(item)
#     return result


# print(get_even(arr))
########################################################################
# Multiply each element of a list by 2
# def multiply_by_2(arr):
#     result = []
#     for item in arr:
#         result.append(item * 2)
#     return result
# def multiply_by_2(arr):
#     for i in range(len(arr)):
#         arr[i] *= 2
#     return arr


# print(arr)
# multiply_by_2(arr)
# print(arr)
########################################################################
# Params in functions
# def f(a):
#     a = a * 2


# a = 4
# f(a)
# print(a)
