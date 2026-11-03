def peak_index_in_mountain_array(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
arr = [0, 2, 5, 3, 1]
print(peak_index_in_mountain_array(arr))
