def count_and_say(n):
    current = "1"
    for _ in range(n - 1):
        result = []
        i = 0
        while i < len(current):
            count = 1
            while i + 1 < len(current) and current[i] == current[i + 1]:
                count += 1
                i += 1
            result.append(str(count))
            result.append(current[i])
            i += 1
        current = "".join(result)
    return current
n = 5
print(count_and_say(n))
