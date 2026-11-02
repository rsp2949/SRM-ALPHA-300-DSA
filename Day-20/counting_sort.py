def counting_sort(s):
    count = [0] * 26
    for ch in s:
        index = ord(ch) - ord('a')
        count[index] += 1
    result = ""
    for i in range(26):
        while count[i] > 0:
            result += chr(i + ord('a'))
            count[i] -= 1
    return result
s = "edsab"
print(counting_sort(s))
