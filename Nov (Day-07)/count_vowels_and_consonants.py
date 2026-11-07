def countVowelsConsonants(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if 'a' <= ch <= 'z':
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants
s = input()
v, c = countVowelsConsonants(s)
print("Vowels:", v)
print("Consonants:", c)
