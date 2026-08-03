from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inv_nums = defaultdict(int)
        for (i, el) in enumerate(nums):
            inv_nums[el] = i

        for (i, el) in enumerate(nums):
            if (inv_nums[target - el] != 0 and inv_nums[target - el] != i):
                return [i, inv_nums[target - el]]
        