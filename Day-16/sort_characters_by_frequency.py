class Solution:
    def frequencySort(self, s):
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        chars = []
        for char in frequency:
            chars.append(char)
        n = len(chars)
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if frequency[chars[j]] > frequency[chars[max_index]]:
                    max_index = j
            if max_index != i:
                temp = chars[i]
                chars[i] = chars[max_index]
                chars[max_index] = temp
        result = []
        for char in chars:
            for _ in range(frequency[char]):
                result.append(char)

        return "".join(result)
