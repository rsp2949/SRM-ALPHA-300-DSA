class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            length = right - left + 1
            if length > max_length:
                max_length = length
        return max_length
