def ship_within_days(weights, days):
    low = max(weights)
    high = sum(weights)
    def can_ship(capacity):
        used_days = 1
        current_load = 0
        for weight in weights:
            if current_load + weight > capacity:
                used_days += 1
                current_load = weight
            else:
                current_load += weight
        return used_days <= days
    while low < high:
        mid = (low + high) // 2
        if can_ship(mid):
            high = mid
        else:
            low = mid + 1
    return low
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(ship_within_days(weights, days))
