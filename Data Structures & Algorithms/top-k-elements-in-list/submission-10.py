class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]

        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for key, val in counts.items():
            buckets[val].append(key)
        
        result = []
        for i in range(n, -1, -1):
            for item in buckets[i]:
                result.append(item)
                if len(result) == k: return result