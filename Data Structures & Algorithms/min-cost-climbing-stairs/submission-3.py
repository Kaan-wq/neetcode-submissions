class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]

        for c in (cost[2:] + [0]):
            prev2, prev1 = prev1, c + min(prev2, prev1)
        return prev1