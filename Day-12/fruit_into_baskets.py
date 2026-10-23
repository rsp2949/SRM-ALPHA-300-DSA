class Solution:
    def totalFruit(self, fruits):
        left = 0
        counts = {}
        max_length = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            if fruit in counts:
                counts[fruit] += 1
            else:
                counts[fruit] = 1

            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1

                if counts[left_fruit] == 0:
                    del counts[left_fruit]

                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length
