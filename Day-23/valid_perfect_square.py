def is_perfect_square(num):
    if num < 1:
        return False
    low = 1
    high = num
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1
    return False
num = 16
print(is_perfect_square(num))
