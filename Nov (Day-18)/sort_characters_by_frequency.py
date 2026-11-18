class Solution:
    def frequencySort(self, s: str) -> str:
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
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        items = merge_sort(items)
        result = ""
        for char, count in items:
            result += char * count
        return result
