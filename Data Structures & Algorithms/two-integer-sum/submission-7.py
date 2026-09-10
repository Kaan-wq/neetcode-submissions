class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duphash = {}
        for i, n in enumerate(nums):
            val = target - n
            if duphash.get(val, -1) != -1:
                return [duphash[val], i]
            duphash[n] = i
        return []