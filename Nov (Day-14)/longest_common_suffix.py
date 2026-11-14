def longestCommonSuffix(strs):
    if len(strs) == 0:
        return ""
    first = strs[0]
    suffix = []
    for i in range(1, len(first) + 1):
        current = first[-i]
        for j in range(1, len(strs)):
            if i > len(strs[j]) or strs[j][-i] != current:
                left = 0
                right = len(suffix) - 1
                while left < right:
                    suffix[left], suffix[right] = suffix[right], suffix[left]
                    left += 1
                    right -= 1
                return "".join(suffix)
        suffix.append(current)
    left = 0
    right = len(suffix) - 1
    while left < right:
        suffix[left], suffix[right] = suffix[right], suffix[left]
        left += 1
        right -= 1
    return "".join(suffix)
n = int(input())
strs = []
for i in range(n):
    strs.append(input())
print(longestCommonSuffix(strs))
