class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}
        for n in nums:
            hist[n] = hist.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in hist.items():
            buckets[c].append(n)

        top_k = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
                    
        return top_k