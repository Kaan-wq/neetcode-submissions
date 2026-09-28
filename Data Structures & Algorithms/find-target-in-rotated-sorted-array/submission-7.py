class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            idx = (hi + lo) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] < nums[hi]:
                if nums[idx] < target <= nums[hi]:
                    lo = idx + 1
                else:
                    hi = idx - 1
            else:
                if nums[lo] <= target < nums[idx]:
                    hi = idx - 1
                else:
                    lo = idx + 1
        return -1