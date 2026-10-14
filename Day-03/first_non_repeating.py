class Solution:
    def nonRepeating(self, arr):
        frequency = {}

        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in arr:
            if frequency[num] == 1:
                return num

        return 0
