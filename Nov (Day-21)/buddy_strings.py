class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            freq = {}
            for char in s:
                freq[char] = freq.get(char, 0) + 1
                if freq[char] > 1:
                    return True
            return False
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) != 2:
            return False
        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
