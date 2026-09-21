class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        best = 0
        for num in nums:
            if num - 1 in hset: continue

            cur = 1
            val = num
            while val + 1 in hset:
                cur += 1
                val += 1
            best = max(best, cur)
        return best