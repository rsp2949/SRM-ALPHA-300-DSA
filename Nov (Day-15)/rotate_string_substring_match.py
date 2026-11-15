def strStr(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1
def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    if len(s) == 0:
        return True
    doubled = s + s
    return strStr(doubled, goal) != -1
s = input()
goal = input()
print(rotateString(s, goal))
