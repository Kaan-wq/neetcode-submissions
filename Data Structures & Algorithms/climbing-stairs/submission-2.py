class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(num: int) -> None:
            if cache.get(num, None): return cache[num]
            if num < 0: return 0
            if num == 0: return 1

            cache[num-1] = dfs(num-1)
            cache[num-2] = dfs(num-2)
            return cache[num-1] + cache[num-2]
            
        
        return dfs(n)