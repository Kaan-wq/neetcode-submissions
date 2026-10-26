class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        cache = [INF] * (amount+1)
        cache[0] = 0
        for r in range(1, amount+1):
            cache[r] = 1 + min(
                (cache[r - coin] for coin in coins if coin <= r),
                default=INF
            )
        return cache[amount] if cache[amount] < INF else -1