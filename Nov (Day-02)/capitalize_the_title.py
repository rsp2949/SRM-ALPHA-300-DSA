def convert_lower(ch):
    value = ord(ch)
    if 65 <= value <= 90:
        return chr(value + 32)
    return ch
def convert_upper(ch):
    value = ord(ch)
    if 97 <= value <= 122:
        return chr(value - 32)
    return ch
def capitalize_title(title):
    result = []
    word = []
    for i in range(len(title) + 1):
        if i == len(title) or title[i] == " ":
            if len(word) <= 2:
                for ch in word:
                    result.append(convert_lower(ch))
            else:
                result.append(convert_upper(word[0]))
                for j in range(1, len(word)):
                    result.append(convert_lower(word[j]))
            word = []
            if i < len(title):
                result.append(" ")
        else:
            word.append(title[i])
    return "".join(result)
title = "capiTalIze tHe titLe"
print(capitalize_title(title))
