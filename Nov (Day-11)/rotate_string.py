def rotateString(s, goal):
    n = len(s)
    if n != len(goal):
        return False
    if n == 0:
        return True
    for start in range(n):
        match = True
        for j in range(n):
            if s[(start + j) % n] != goal[j]:
                match = False
                break
        if match:
            return True
    return False
s = input()
goal = input()
print(rotateString(s, goal))
