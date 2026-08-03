from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for item in nums:
            if (counts[item] > 0): return True
            counts[item] += 1
        return False
