class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_s = {}
        freq_target = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in target:
            freq_target[char] = freq_target.get(char, 0) + 1
        result = float("inf")
        for char in freq_target:
            if char not in freq_s:
                return 0
            count = freq_s[char] // freq_target[char]
            if count < result:
                result = count
        return result
