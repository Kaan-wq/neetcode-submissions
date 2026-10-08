from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        r = []
        for i, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            d.append(i)

            if d[0] + k - 1 < i:
                d.popleft()
            
            if i >= k - 1:
                r.append(nums[d[0]])
        return r
