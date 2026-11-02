def sort_zeros_ones(arr):
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
    for i in range(len(arr)):
        if i < zero_count:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr
arr = [1, 0, 1, 0, 0, 1]
sort_zeros_ones(arr)
print(arr)
