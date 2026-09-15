from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()          # indices, values decreasing
        res = []
        for r, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(r)
            if dq[0] <= r - k:        # front expired
                dq.popleft()
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res