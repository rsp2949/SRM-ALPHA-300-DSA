def compress(chars):
    read = 0
    write = 0
    n = len(chars)
    while read < n:
        current = chars[read]
        count = 0
        while read < n and chars[read] == current:
            count += 1
            read += 1
        chars[write] = current
        write += 1
        if count > 1:
            digits = []
            while count > 0:
                digits.append(chr(count % 10 + 48))
                count //= 10
            left = 0
            right = len(digits) - 1
            while left < right:
                digits[left], digits[right] = digits[right], digits[left]
                left += 1
                right -= 1
            for digit in digits:
                chars[write] = digit
                write += 1
    return write
chars = list(input())
length = compress(chars)
print(length)
print("".join(chars[:length]))
