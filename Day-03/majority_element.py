class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in nums:
            if frequency[num] > len(nums) // 2:
                return num
