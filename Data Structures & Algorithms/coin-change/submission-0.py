class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(r: int):
            if r in cache: return cache[r]
            if r < 0: return float("inf")
            if r == 0: return 0

            val = float("inf")
            for coin in coins:
                val = min(val, 1+dfs(r-coin))
            cache[r] = val
            return cache[r]
        result = dfs(amount)
        return result if result < float("inf") else -1