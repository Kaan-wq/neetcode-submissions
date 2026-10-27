class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        max_ = min_ = 1
        for num in nums:
            ext_max_, ext_min_ = num * max_, num * min_
            max_, min_ = max(num, ext_max_, ext_min_), min(num, ext_max_, ext_min_)
            best = max(best, max_)
        return best