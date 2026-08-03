from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for el in nums:
            counts[el] += 1
        return sorted(counts, key=lambda k: counts[k], reverse=True)[:k]