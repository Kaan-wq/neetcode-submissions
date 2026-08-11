class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        profits = []
        for i in range(1, len(prices)):
            profit = prices[i] - prices[p1]
            print(profit)
            if profit < 0:
                p1 = i
            else:
                profits.append(profit)
        return max(profits) if profits else 0