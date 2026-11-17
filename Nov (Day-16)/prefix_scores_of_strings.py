class Solution:
    def sumPrefixScores(self, words):
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {"count": 0}
                node = node[ch]
                node["count"] += 1
        result = []
        for word in words:
            node = trie
            score = 0
            for ch in word:
                node = node[ch]
                score += node["count"]
            result.append(score)
        return result
