class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = 0
        for sell, price in enumerate(prices):
            if price >= prices[buy]:
                profit = max(profit, price - prices[buy])
            else:
                buy = sell
        return profit
