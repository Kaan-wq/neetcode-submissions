class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(r: int) -> float:
            if r in cache: return cache[r]
            if r == 0: return 0

            best = min(
                (dfs(r - coin) for coin in coins if coin <= r),
                default=float("inf")
            )
            cache[r] = best + 1
            return cache[r]
        result = dfs(amount)
        return result if result < float("inf") else -1