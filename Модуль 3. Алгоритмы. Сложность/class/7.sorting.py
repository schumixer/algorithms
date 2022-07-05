arr = [1, 7, 9, 10, 4, 7, 8, 2, 3, 5]


# def bubble_sort(arr: list) -> None:
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


# bubble_sort(arr)
###################################################
# def get_smallest_index(arr: list) -> int:
#     smallest_index = 0
#     for i in range(len(arr)):
#         if arr[i] < arr[smallest_index]:
#             smallest_index = i
#     return smallest_index


# def selection_sort(arr: list) -> list:
#     sorted_arr = []
#     for _ in range(len(arr)):
#         smallest_index = get_smallest_index(arr)
#         sorted_arr.append(arr.pop(smallest_index))
#     return sorted_arr


# print(selection_sort(arr))
###################################################
# quick sort
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(arr))
