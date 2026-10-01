class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            idx = i
            while stack and stack[-1][1] > h:
                j, height = stack.pop()
                best = max(best, (i - j) * height)
                idx = j
            stack.append((idx, h))
        return best