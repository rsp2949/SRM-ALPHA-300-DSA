def k_smallest(arr, k):
    n = len(arr)
    if k < 0 or k > n:
        return []
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    result = []
    for i in range(k):
        result.append(arr[i])
    return result
