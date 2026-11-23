class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = {}
        freq2 = {}
        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1
        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1
        for char in freq1:
            if char not in freq2:
                return False
        counts1 = {}
        counts2 = {}
        for count in freq1.values():
            counts1[count] = counts1.get(count, 0) + 1
        for count in freq2.values():
            counts2[count] = counts2.get(count, 0) + 1
        return counts1 == counts2
