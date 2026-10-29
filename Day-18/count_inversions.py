class Solution:
    def inversionCount(self, arr):
        def merge_sort_count(left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = merge_sort_count(left, mid)
            count += merge_sort_count(mid, right)
            temp = []
            i = left
            j = mid
            while i < mid and j < right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    count += mid - i
                    j += 1
            while i < mid:
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            for k in range(len(temp)):
                arr[left + k] = temp[k]
            return count
        return merge_sort_count(0, len(arr))
sol = Solution()
print(sol.inversionCount([2, 4, 1, 3, 5]))
print(sol.inversionCount([2, 3, 4, 5, 6]))
print(sol.inversionCount([10, 10, 10]))
print(sol.inversionCount([5, 4, 3, 2, 1]))
