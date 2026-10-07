class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0] * n, [0] * n

        left_max = height[0]
        for i in range(n):
            left_max = max(left_max, height[i])
            left[i] = left_max

        right_max = height[n - 1]
        for i in reversed(range(n)):
            right_max = max(right_max, height[i])
            right[i] = right_max
        
        water = 0
        for i, h in enumerate(height):
            water += min(left[i], right[i]) - h
        return water