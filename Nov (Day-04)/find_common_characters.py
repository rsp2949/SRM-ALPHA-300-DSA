def common_chars(words):
    common = {}
    for ch in words[0]:
        common[ch] = common.get(ch, 0) + 1
    for word in words[1:]:
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in common:
            common[ch] = min(common[ch], freq.get(ch, 0))
    result = []
    for ch in common:
        for _ in range(common[ch]):
            result.append(ch)
    return result
words = ["bella", "label", "roller"]
print(common_chars(words))
