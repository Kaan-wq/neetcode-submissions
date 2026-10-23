class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers: List[int]) -> int:
            prev1 = prev2 = 0
            for num in numbers:
                prev1, prev2 = max(num + prev2, prev1), prev1
            return prev1
        if len(nums) == 1: return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))