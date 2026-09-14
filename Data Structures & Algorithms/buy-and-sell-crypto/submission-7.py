class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0
        for i in range(1, len(prices)):
            if prices[left] > prices[i]:
                left = i
            best = max(best, prices[i] - prices[left])
        return best