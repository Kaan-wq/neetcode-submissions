class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0 for _ in range(n)]
        r = [0 for _ in range(n)]
        l[0] = height[0]
        r[-1] = height[-1]
        for i in range(1, n):
            l[i] = max(l[i-1], height[i])
            r[-i-1] = max(r[-i], height[-i-1]) 

        water = 0
        for i in range(n):
            water += min(r[i], l[i]) - height[i]
        return water