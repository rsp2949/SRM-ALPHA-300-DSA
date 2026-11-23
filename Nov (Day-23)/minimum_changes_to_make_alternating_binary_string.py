class Solution:
    def minOperations(self, s: str) -> int:
        changes1 = 0
        changes2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    changes1 += 1
                if s[i] != '1':
                    changes2 += 1
            else:
                if s[i] != '1':
                    changes1 += 1
                if s[i] != '0':
                    changes2 += 1
        return min(changes1, changes2)
