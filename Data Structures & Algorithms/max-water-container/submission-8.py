class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            lh, rh = heights[l], heights[r]
            best = max(best, min(lh, rh) * (r - l))
            if lh < rh:
                l += 1
            else:
                r -= 1
        return best