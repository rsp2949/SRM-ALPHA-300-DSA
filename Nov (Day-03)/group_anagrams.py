def group_anagrams(strs):
    groups = {}
    for word in strs:
        freq = [0] * 26
        for ch in word:
            index = ord(ch) - ord('a')
            freq[index] += 1
        key = tuple(freq)
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
