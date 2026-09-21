class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        
        result = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k: return result
        return result