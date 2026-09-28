class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []
        for i, h in enumerate(heights + [0]):
            idx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                best = max(best, (i - idx) * height)
            stack.append((idx, h))
        return best