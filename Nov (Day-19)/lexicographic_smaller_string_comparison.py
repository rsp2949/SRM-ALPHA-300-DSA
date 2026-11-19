class Solution:
    def countSmallerStrings(self, words: list[str], target: str) -> int:
        left = 0
        right = len(words)
        while left < right:
            mid = (left + right) // 2
            if words[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
