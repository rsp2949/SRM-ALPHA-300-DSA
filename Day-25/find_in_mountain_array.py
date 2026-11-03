class MountainArray:
    def __init__(self, arr):
        self.arr = arr
    def get(self, index):
        return self.arr[index]
    def length(self):
        return len(self.arr)
def find_in_mountain_array(target, mountain_arr):
    n = mountain_arr.length()
    low = 0
    high = n - 1
    while low < high:
        mid = low + (high - low) // 2
        if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            low = mid + 1
        else:
            high = mid
    peak = low
    low = 0
    high = peak
    while low <= high:
        mid = low + (high - low) // 2
        value = mountain_arr.get(mid)
        if value == target:
            return mid
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    low = peak + 1
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        value = mountain_arr.get(mid)
        if value == target:
            return mid
        elif value > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
mountain_arr = MountainArray([1, 2, 3, 4, 5, 3, 1])
target = 3
print(find_in_mountain_array(target, mountain_arr))
