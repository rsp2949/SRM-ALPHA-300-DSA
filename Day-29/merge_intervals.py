def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def merge_intervals(intervals):
    intervals = merge_sort(intervals)
    if not intervals:
        return []
    result = [intervals[0][:]]
    for current in intervals[1:]:
        if current[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], current[1])
        else:
            result.append(current[:])
    return result
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
