class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(string):
            if len(string) < 2:
                return ""
            chars = set(string)
            for i, char in enumerate(string):
                if char.swapcase() not in chars:
                    left = solve(string[:i])
                    right = solve(string[i + 1:])
                    if len(left) >= len(right):
                        return left
                    return right
            return string
        return solve(s)
