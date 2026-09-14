from itertools import accumulate

class Solution:
    def trap(self, height: List[int]) -> int:
        left = list(accumulate(height, max))
        right = list(accumulate(reversed(height), max))[::-1]
        return sum(min(a, b) - h for a, b, h in zip(left, right, height))