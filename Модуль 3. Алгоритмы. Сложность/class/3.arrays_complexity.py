arr = [1, 9, 8, 7, 5, 3]
print(arr[0], "access: O(1)")
print(arr.index(8), "search: O(n)")
print(arr.pop(0), "deletion: O(n)")
print(arr)
print(arr.append(8), "insertion: O(1)")
print(arr.insert(0, 76), "insertion: O(n)")
print(arr)
