def row_with_max_ones(arr):
    rows = len(arr)
    cols = len(arr[0])
    max_count = 0
    result = -1
    for i in range(rows):
        low = 0
        high = cols - 1
        first = cols
        while low <= high:
            mid = (low + high) // 2
            if arr[i][mid] == 1:
                first = mid
                high = mid - 1
            else:
                low = mid + 1
        count = cols - first
        if count > max_count:
            max_count = count
            result = i
    return result
arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
print(row_with_max_ones(arr))
