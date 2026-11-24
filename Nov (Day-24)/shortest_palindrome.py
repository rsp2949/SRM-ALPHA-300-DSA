class Solution:
    def shortestPalindrome(self, s: str) -> str:
        end = len(s)
        while end > 0:
            left = 0
            right = end - 1
            is_palindrome = True
            while left < right:
                if s[left] != s[right]:
                    is_palindrome = False
                    break
                left += 1
                right -= 1
            if is_palindrome:
                break
            end -= 1
        result = []
        for i in range(len(s) - 1, end - 1, -1):
            result.append(s[i])
        return "".join(result) + s
