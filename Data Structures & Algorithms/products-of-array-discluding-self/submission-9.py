class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]
        for i in range(1, len(nums)):
            out.append(nums[i-1] * out[i - 1])
        cum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] *= cum
            cum *= nums[i]
        return out