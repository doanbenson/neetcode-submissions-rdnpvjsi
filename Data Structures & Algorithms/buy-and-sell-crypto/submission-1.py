class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        buy_day, sell_day = 0, 1

        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                best_profit = max(best_profit, profit)
            else:
                buy_day = sell_day 
            sell_day += 1
        
        return best_profit