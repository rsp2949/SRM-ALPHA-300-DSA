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
        if left[i][1] <= right[j][1]:
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
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals = merge_sort(intervals)
    removals = 0
    last_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            removals += 1
        else:
            last_end = intervals[i][1]
    return removals
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(erase_overlap_intervals(intervals))
