class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        n = len(s)
        for count in freq.values():
            if count > (n + 1) // 2:
                return ""
        result = []
        previous = ""
        for _ in range(n):
            best_char = ""
            best_count = 0
            for char in freq:
                if char != previous and freq[char] > best_count:
                    best_char = char
                    best_count = freq[char]
            if best_char == "":
                return ""
            result.append(best_char)
            freq[best_char] -= 1
            previous = best_char
        return "".join(result)
