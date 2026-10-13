def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = None
    second = None
    for num in nums:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second
print(second_largest([12, 35, 1, 10, 34, 1]))
print(second_largest([10, 5, 10]))
print(second_largest([1, 2]))
print(second_largest([5, 5, 5]))
print(second_largest([-1, -5, -3]))
