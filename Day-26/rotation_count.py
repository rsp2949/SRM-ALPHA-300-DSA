def rotation_count(arr):
    if len(arr) == 0:
        return 0
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low
arr = [5, 1, 2, 3, 4]
print(rotation_count(arr))
