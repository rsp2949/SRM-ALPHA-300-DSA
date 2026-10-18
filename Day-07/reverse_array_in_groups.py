class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)
        start = 0

        while start < n:
            left = start
            right = start + k - 1

            if right >= n:
                right = n - 1

            while left < right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1

            start += k

        return arr
