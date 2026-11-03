def longest_common_prefix(strs):
    if not strs:
        return ""
    result = []
    for i in range(len(strs[0])):
        ch = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != ch:
                return "".join(result)
        result.append(ch)
    return "".join(result)
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))
