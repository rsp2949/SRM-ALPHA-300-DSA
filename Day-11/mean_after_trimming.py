class Solution:
    def trimMean(self, arr):
        n = len(arr)
        remove_count = n // 20

        frequency = [0] * 100001
        total = 0

        for num in arr:
            frequency[num] += 1
            total += num

        remaining = remove_count
        value = 0

        while remaining > 0:
            if frequency[value] > 0:
                take = frequency[value]

                if take > remaining:
                    take = remaining

                total -= value * take
                frequency[value] -= take
                remaining -= take

            value += 1

        remaining = remove_count
        value = 100000

        while remaining > 0:
            if frequency[value] > 0:
                take = frequency[value]

                if take > remaining:
                    take = remaining

                total -= value * take
                frequency[value] -= take
                remaining -= take

            value -= 1

        return total / (n - 2 * remove_count)
