class Solution:
    def intersection(self, nums1, nums2):
        result = []
        for num in nums1:
            if num not in result:
                found = False
                for value in nums2:
                    if num == value:
                        found = True
                        break
                if found:
                    result.append(num)
        return result
