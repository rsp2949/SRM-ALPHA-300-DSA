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
        if left[i] <= right[j]:
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
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
def longest_consecutive(nums):
    if not nums:
        return 0
    nums = merge_sort(nums)
    unique = []
    for num in nums:
        if not unique or unique[-1] != num:
            unique.append(num)
    longest = 0
    for num in unique:
        if not binary_search(unique, num - 1):
            count = 1
            current = num
            while binary_search(unique, current + 1):
                current += 1
                count += 1
            longest = max(longest, count)
    return longest
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))
