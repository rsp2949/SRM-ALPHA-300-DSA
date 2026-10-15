class Solution:
    def maxProfit(self, prices):
        minimum_price = prices[0]
        best_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            else:
                profit = prices[i] - minimum_price
                if profit > best_profit:
                    best_profit = profit

        return best_profit
