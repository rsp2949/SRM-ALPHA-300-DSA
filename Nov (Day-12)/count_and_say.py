def countAndSay(n):
    result = "1"
    for step in range(n - 1):
        parts = []
        i = 0
        while i < len(result):
            current = result[i]
            count = 0
            while i < len(result) and result[i] == current:
                count += 1
                i += 1
            parts.append(str(count))
            parts.append(current)
        result = "".join(parts)
    return result
n = int(input())
print(countAndSay(n))
