class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        result = []
        for char in order:
            if char in freq:
                result.append(char * freq[char])
                del freq[char]
        for char in freq:
            result.append(char * freq[char])
        return "".join(result)
