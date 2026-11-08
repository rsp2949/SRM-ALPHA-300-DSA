def reverseWords(s):
    words = []
    current = []
    for ch in s:
        if ch != ' ':
            current.append(ch)
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    left = 0
    right = len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)
s = input()
print(reverseWords(s))
