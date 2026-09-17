class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                warmer[idx] = i - idx
            stack.append(i)
        return warmer