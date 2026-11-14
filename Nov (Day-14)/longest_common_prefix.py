def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    first = strs[0]
    prefix = []
    for i in range(len(first)):
        current = first[i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != current:
                return "".join(prefix)
        prefix.append(current)
    return "".join(prefix)
n = int(input())
strs = []
for i in range(n):
    strs.append(input())
print(longestCommonPrefix(strs))
