class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        if len(p) > len(s):
            return result
        freq = {}
        for char in p:
            freq[char] = freq.get(char, 0) + 1
        window = {}
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if right >= len(p):
                left_char = s[right - len(p)]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            if window == freq:
                result.append(right - len(p) + 1)
        return result
