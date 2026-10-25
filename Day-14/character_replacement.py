class Solution:
    def characterReplacement(self, s, k):
        left = 0
        counts = {}
        max_freq = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
            if counts[char] > max_freq:
                max_freq = counts[char]
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1
            length = right - left + 1
            if length > max_length:
                max_length = length
        return max_length
