class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1] * (n+1)
        for idx in range(2, n+1): cache[idx] = cache[idx-1] + cache[idx-2]
        return cache[n]
