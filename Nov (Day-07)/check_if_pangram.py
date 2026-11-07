
def checkIfPangram(sentence):
    letters = set()
    for ch in sentence:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        if 'a' <= ch <= 'z':
            letters.add(ch)
    return len(letters) == 26
sentence = input()
print(checkIfPangram(sentence))
