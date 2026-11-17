class Solution:
    def countVowels(self, s, queries):
        vowels = "aeiou"
        prefix = [0]
        for ch in s:
            count = 1 if ch in vowels else 0
            prefix.append(prefix[-1] + count)
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] - prefix[left])
        return result
