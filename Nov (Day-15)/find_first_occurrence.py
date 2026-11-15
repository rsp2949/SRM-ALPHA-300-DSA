def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1
haystack = input()
needle = input()
print(strStr(haystack, needle))
