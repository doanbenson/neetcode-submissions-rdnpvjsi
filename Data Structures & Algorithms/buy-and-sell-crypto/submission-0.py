class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                l = r
        
        return max_profit

