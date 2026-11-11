def rotateByK(s, k):
    n = len(s)
    if n == 0:
        return s
    k = k % n
    result = [''] * n
    for i in range(n):
        new_index = (i + k) % n
        result[new_index] = s[i]
    return "".join(result)
s = input()
k = int(input())
print(rotateByK(s, k))
