class Solution:
    def rob(self, nums: List[int]) -> int:
        cache, n = {}, len(nums)
        def dfs(n: int):
            if n in cache: return cache[n]
            if n < 0: return 0

            cache[n] = max(nums[n] + dfs(n-2), dfs(n-1))
            return cache[n]
        return dfs(n-1)