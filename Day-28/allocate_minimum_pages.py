def allocate_pages(arr, k):
    if k > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    def can_allocate(limit):
        students = 1
        pages = 0
        for book in arr:
            if pages + book > limit:
                students += 1
                pages = book
            else:
                pages += book
        return students <= k
    while low < high:
        mid = (low + high) // 2
        if can_allocate(mid):
            high = mid
        else:
            low = mid + 1
    return low
arr = [12, 34, 67, 90]
k = 2

print(allocate_pages(arr, k))
