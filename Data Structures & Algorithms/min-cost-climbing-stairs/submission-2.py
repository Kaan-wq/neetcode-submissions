class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(n: int) -> int:
            if n in cache: return cache[n]
            if n < 2: return 0

            cache[n] = min(cost[n-1] + dfs(n-1), cost[n-2] + dfs(n-2))
            return cache[n]
        return dfs(len(cost))