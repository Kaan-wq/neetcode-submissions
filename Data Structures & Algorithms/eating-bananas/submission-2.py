class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, max(piles)
        best_k = hi
        while lo <= hi:
            k = (hi + lo) // 2
            if k == 0: return best_k
            hours = h
            for banana in piles:
                hours -= (banana + k - 1) // k
            if hours < 0:
                lo = k + 1
            elif hours >= 0:
                hi = k - 1
                best_k = min(best_k, k)
        return best_k