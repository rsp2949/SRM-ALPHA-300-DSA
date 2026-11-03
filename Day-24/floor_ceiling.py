def floor_ceiling(arr, target):
    floor = -1
    ceiling = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            ceiling = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return [floor, ceiling]
arr = [1, 2, 4, 6, 10, 12, 14]
target = 5
print(floor_ceiling(arr, target))
