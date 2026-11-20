class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = {}
        window = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        left = 0
        matched = 0
        start = 0
        min_length = float("inf")
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                matched += 1
            while matched == len(need):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    matched -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        return s[start:start + min_length]
