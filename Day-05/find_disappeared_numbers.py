class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        present = [False] * (n + 1)

        for num in nums:
            present[num] = True

        result = []

        for i in range(1, n + 1):
            if not present[i]:
                result.append(i)

        return result
