class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [0] * n
        cache[0], cache[1] = cost[0], cost[1]

        for idx in range(2, n):
            cache[idx] = cost[idx] + min(cache[idx-1], cache[idx-2])
        return min(cache[n-1], cache[n-2])