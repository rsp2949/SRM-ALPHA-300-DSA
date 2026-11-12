def reversePrefix(word, ch):
    position = -1
    for i in range(len(word)):
        if word[i] == ch:
            position = i
            break
    if position == -1:
        return word
    chars = list(word)
    left = 0
    right = position
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)
word = input()
ch = input()
print(reversePrefix(word, ch))
