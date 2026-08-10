class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_area = 0

        for i in range(n):
            h_l = heights[l]
            h_r = heights[r]
            
            if h_l <= h_r:
                max_area = max(max_area, (r - l) * min(h_l, h_r))
                l += 1
            else:
                max_area = max(max_area, (r - l) * min(h_l, h_r))
                r -= 1

        return max_area