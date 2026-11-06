def can_permute_palindrome(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    odd_count = 0
    for count in freq.values():
        if count % 2 == 1:
            odd_count += 1
    return odd_count <= 1
s = "aab"
print(can_permute_palindrome(s))
