def reverseStr(s, k):
    chars = list(s)
    n = len(chars)
    start = 0
    while start < n:
        left = start
        right = min(start + k - 1, n - 1)
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        start += 2 * k
    return "".join(chars)
s = input()
k = int(input())
print(reverseStr(s, k))
