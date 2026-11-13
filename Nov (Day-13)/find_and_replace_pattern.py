def matches(word, pattern):
    if len(word) != len(pattern):
        return False
    mapPTW = {}
    mapWTP = {}
    for i in range(len(pattern)):
        p = pattern[i]
        w = word[i]
        if p in mapPTW:
            if mapPTW[p] != w:
                return False
        else:
            mapPTW[p] = w
        if w in mapWTP:
            if mapWTP[w] != p:
                return False
        else:
            mapWTP[w] = p
    return True
def findAndReplacePattern(words, pattern):
    result = []
    for word in words:
        if matches(word, pattern):
            result.append(word)
    return result
words = input().split()
pattern = input()
print(findAndReplacePattern(words, pattern))
