class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        items = list(freq.items())
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i][1] >= right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1
            return result
        items = merge_sort(items)
        if items[0][1] > (len(s) + 1) // 2:
            return ""
        result = [""] * len(s)
        index = 0
        for char, count in items:
            for _ in range(count):
                if index >= len(s):
                    index = 1
                result[index] = char
                index += 2
        return "".join(result)
