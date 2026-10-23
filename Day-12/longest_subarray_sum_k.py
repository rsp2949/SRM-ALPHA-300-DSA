class Solution:
    def longestSubarray(self, arr, k):
        left = 0
        window_sum = 0
        max_length = 0

        for right in range(len(arr)):
            window_sum += arr[right]

            while left <= right and window_sum > k:
                window_sum -= arr[left]
                left += 1

            if window_sum == k:
                length = right - left + 1

                if length > max_length:
                    max_length = length

        return max_length
