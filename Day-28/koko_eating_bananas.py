def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    def can_finish(speed):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + speed - 1) // speed
        return total_hours <= h
    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1
    return low
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))
