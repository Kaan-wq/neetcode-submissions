class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0
        for i in range(1, len(prices)):
            while prices[left] > prices[i]:
                left += 1
            best = max(best, prices[i] - prices[left])
        return best