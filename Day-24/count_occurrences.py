def count_occurrences(arr, target):
    first = -1
    last = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if first == -1:
        return 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last - first + 1
arr = [1, 1, 2, 2, 2, 2, 3]
target = 2

print(count_occurrences(arr, target))
