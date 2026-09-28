class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []

        for i, h in enumerate(heights):
            idx = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                area = (i - idx) * height
                best = max(best, area)
            stack.append((idx, h))

        while stack:
            idx, height = stack.pop()
            area = (len(heights) - idx) * height
            best = max(best, area)
        return best