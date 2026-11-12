def encode(strs):
    result = []
    for word in strs:
        result.append(str(len(word)))
        result.append('#')
        result.append(word)
    return "".join(result)
def decode(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        length = 0
        while s[i] != '#':
            length = length * 10 + ord(s[i]) - 48
            i += 1
        i += 1
        word = s[i:i + length]
        result.append(word)
        i += length
    return result
strs = input().split()
encoded = encode(strs)
print("Encoded:", encoded)
print("Decoded:", decode(encoded))
