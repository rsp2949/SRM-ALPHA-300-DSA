def isVowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'
def reverseVowels(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1
    while left < right:
        if not isVowel(chars[left]):
            left += 1
        elif not isVowel(chars[right]):
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)
s = input()
print(reverseVowels(s))
