class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = []
        d = collections.deque()
        l = 0

        for r in range(len(nums)):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)

            if (r - l + 1) < k:
                continue

            if l > d[0]:
                d.popleft()

            maximum.append(nums[d[0]])
            l += 1    
        
        return maximum