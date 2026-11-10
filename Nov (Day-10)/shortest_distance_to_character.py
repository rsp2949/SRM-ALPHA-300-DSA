def shortestToChar(s, c):
    n = len(s)
    answer = [n] * n
    previous = -n
    for i in range(n):
        if s[i] == c:
            previous = i
        answer[i] = i - previous
    next_position = 2 * n
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            next_position = i
        distance = next_position - i
        if distance < answer[i]:
            answer[i] = distance
    return answer
s = input()
c = input()
print(shortestToChar(s, c))
