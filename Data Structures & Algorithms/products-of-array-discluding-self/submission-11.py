from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = list(accumulate(nums, mul, initial=1))
        out.pop()
        cum = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= cum
            cum *= nums[i]
        return out