class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = []
        dq = collections.deque()

        for r, el in enumerate(nums):
            while dq and nums[dq[-1]] < el:
                dq.pop()
            dq.append(r)

            if r - k + 1 > dq[0]:
                dq.popleft()

            if r + 1 >= k:
                maximum.append(nums[dq[0]])   
        
        return maximum