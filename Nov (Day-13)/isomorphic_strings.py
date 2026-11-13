def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    mapST = {}
    mapTS = {}
    for i in range(len(s)):
        a = s[i]
        b = t[i]
        if a in mapST:
            if mapST[a] != b:
                return False
        else:
            mapST[a] = b
        if b in mapTS:
            if mapTS[b] != a:
                return False
        else:
            mapTS[b] = a
    return True
s = input()
t = input()
print(isIsomorphic(s, t))
