def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        a = s[left]
        b = s[right]
        if 'A' <= a <= 'Z':
            a = chr(ord(a) + 32)
        if 'A' <= b <= 'Z':
            b = chr(ord(b) + 32)
        if a != b:
            return False
        left += 1
        right -= 1
    return True
s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))
