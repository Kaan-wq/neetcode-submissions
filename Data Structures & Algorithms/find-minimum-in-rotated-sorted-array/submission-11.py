class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        best = float("inf")
        while lo <= hi:
            idx = (hi + lo) // 2
            best = min(best, nums[idx])
            if nums[idx] < nums[hi]:
                hi = idx - 1
            else:
                lo = idx + 1
        return best