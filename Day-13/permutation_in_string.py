class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        for char in s1:
            if char in target:
                target[char] += 1
            else:
                target[char] = 1

        left = 0

        for right in range(len(s2)):
            char = s2[right]

            if char in window:
                window[char] += 1
            else:
                window[char] = 1

            if right - left + 1 > len(s1):
                outgoing = s2[left]
                window[outgoing] -= 1

                if window[outgoing] == 0:
                    del window[outgoing]

                left += 1

            if right - left + 1 == len(s1) and window == target:
                return True

        return False
