class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        present = [False] * (n + 1)

        for num in nums:
            present[num] = True

        for i in range(n + 1):
            if not present[i]:
                return i

        return -1
