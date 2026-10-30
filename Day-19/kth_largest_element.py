class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        def partition(low, high):
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        low = 0
        high = len(nums) - 1
        while low <= high:
            pivot_index = partition(low, high)
            if pivot_index == target:
                return nums[pivot_index]
            elif pivot_index < target:
                low = pivot_index + 1
            else:
                high = pivot_index - 1
sol = Solution()
print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(sol.findKthLargest([7], 1))
