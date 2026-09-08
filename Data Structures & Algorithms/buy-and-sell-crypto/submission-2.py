class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        state = []
        left = 0
        best = 0

        for right in range(len(prices)):
            state.append(prices[right])

            while not prices[left] <= state[-1]:
                state.pop(0)
                left += 1

            best = max(best, prices[right] - prices[left])
        return best