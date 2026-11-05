def is_palindrome(x):
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    reversed_num = 0
    while x > reversed_num:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return x == reversed_num or x == reversed_num // 10
x = 121
print(is_palindrome(x))
