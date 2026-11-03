def to_lower_case(s):
    result = []
    for ch in s:
        value = ord(ch)
        if 65 <= value <= 90:
            value += 32
        result.append(chr(value))
    return "".join(result)
s = "Hello"
print(to_lower_case(s))
