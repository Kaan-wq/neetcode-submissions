class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        cum = 1
        for i in range(1, len(nums)):
            cum *= nums[i - 1]
            out.append(cum)
        cum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] *= cum
            cum *= nums[i]
        return out