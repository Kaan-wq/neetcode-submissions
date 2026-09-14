class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm = rm = water = 0
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                water += lm - height[l]
                l += 1
            else:
                rm = max(rm, height[r])
                water += rm - height[r]
                r -= 1
        return water