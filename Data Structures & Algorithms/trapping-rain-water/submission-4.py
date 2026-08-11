class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l = 0
        r = n - 1

        prefix = [0] * n
        suffix = [0] * n
        prefix[l] = height[l]
        suffix[r] = height[r]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
            suffix[-i - 1] = max(suffix[-i], height[-i - 1])

        water = 0
        for i in range(n):
            water += min(prefix[i], suffix[i]) - height[i]
        return water