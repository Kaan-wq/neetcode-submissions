class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(num: int) -> int:
            if num in cache: return cache[num]
            if num < 0: return 0
            if num == 0: return 1

            cache[num] = dfs(num-1) + dfs(num-2)
            return cache[num]
        return dfs(n)