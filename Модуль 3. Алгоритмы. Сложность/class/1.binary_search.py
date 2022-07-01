# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# O(n)
# if n == 32:
# 32
# binary search
# O(log2(n))
# if n == 32:
# 5
# arr = list(range(1, 101))

# arr = [5, 9, 11, 14, 15, 16]


# def binary_search(arr: list, n: int) -> int:
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == n:
#             return mid
#         elif arr[mid] < n:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# print(binary_search(arr, 11))
# 1s
# n = 8
# 8s 3s
# n = 1000
# 1000s 10s