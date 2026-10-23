class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for idx in range(2, len(cost)):
            prev2, prev1 = prev1, cost[idx] + min(prev2, prev1)
        return min(prev2, prev1)