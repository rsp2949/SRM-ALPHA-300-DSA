def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    mapPW = {}
    mapWP = {}
    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]
        if ch in mapPW:
            if mapPW[ch] != word:
                return False
        else:
            mapPW[ch] = word
        if word in mapWP:
            if mapWP[word] != ch:
                return False
        else:
            mapWP[word] = ch
    return True
pattern = input()
s = input()
print(wordPattern(pattern, s))
