class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        best_k = hi
        while lo <= hi:
            k = (hi + lo) // 2
            hours = sum((pile + k - 1) // k for pile in piles)
            if hours > h:
                lo = k + 1
            else:
                hi = k - 1
                best_k = k
        return best_k