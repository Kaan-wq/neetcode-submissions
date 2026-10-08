from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        for i, num in enumerate(nums):
            if d and d[0] + k - 1 < i:
                d.popleft()
            while d and nums[d[-1]] < num:
                d.pop()
            d.append(i)
            if i >= k - 1:
                result.append(nums[d[0]])
        return result