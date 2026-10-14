def count_frequencies(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
print(count_frequencies([2, 3, 2, 5, 3, 2]))
