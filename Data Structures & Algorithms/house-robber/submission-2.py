class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        for idx in range(len(nums)):
            prev1, prev2 = max(nums[idx] + prev2, prev1), prev1
        return prev1