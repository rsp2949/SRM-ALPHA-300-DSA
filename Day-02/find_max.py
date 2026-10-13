def find_max(nums):
    if len(nums) == 0:
        return None
    maximum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
    return maximum
print(find_max([3, 8, 2, 10, 5]))
print(find_max([-5, -2, -9]))
print(find_max([7]))
print(find_max([4, 4, 4]))
print(find_max([]))
