class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        target = {}
        window = {}

        for char in p:
            if char in target:
                target[char] += 1
            else:
                target[char] = 1

        result = []
        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if right - left + 1 > len(p):
                outgoing = s[left]
                window[outgoing] -= 1

                if window[outgoing] == 0:
                    del window[outgoing]

                left += 1

            if right - left + 1 == len(p) and window == target:
                result.append(left)

        return result
