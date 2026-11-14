def isPrefix(s, prefix):
    if len(prefix) > len(s):
        return False
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True
s = input()
prefix = input()
print(isPrefix(s, prefix))
