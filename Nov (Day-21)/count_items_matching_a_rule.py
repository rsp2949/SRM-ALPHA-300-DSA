class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        keys = ["type", "color", "name"]
        index = keys.index(ruleKey)
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count
