first_bad = 4
def isBadVersion(version):
    return version >= first_bad
def first_bad_version(n):
    low = 1
    high = n
    while low < high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low
n = 5
print(first_bad_version(n))
