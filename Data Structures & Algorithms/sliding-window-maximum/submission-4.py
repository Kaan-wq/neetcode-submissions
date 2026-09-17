class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()

        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] < x:
                dq.pop()
            dq.append(i)

            if i - k + 1 > dq[0]: dq.popleft()

            if i + 1 >= k: res.append(nums[dq[0]])   
        return res