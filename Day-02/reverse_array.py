def reverse_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums
print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([1, 2]))
print(reverse_array([7]))
print(reverse_array([]))
print(reverse_array([1, 2, 2, 3]))
