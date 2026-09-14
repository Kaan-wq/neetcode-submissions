class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm = rm = water = 0
        while l < r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])
            if lm < rm:
                water += lm - height[l]
                l += 1
            else:
                water += rm - height[r]
                r -= 1
        return water