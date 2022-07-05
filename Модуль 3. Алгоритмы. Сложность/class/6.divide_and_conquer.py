# def sum_array_dc(arr: list) -> int:
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sum_array_dc(arr[1:])


arr = [1, 6, 5, 4, 3, 8, 9, 3, 2]
# arr = [-5, -7, -3, -1, -2, -4]
# print(sum_array_dc(arr) == sum(arr))
###############################################################################
def max_element(arr: list) -> int:
    # if len(arr) == 0:
    #     return float("-inf")
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_element(arr[1:]))


print(max_element(arr))
