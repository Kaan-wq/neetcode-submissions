class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        best = 0
        for num in nums:
            if num - 1 in hset:
                continue

            end = num + 1
            while end in hset:
                end += 1
            best = max(best, end - num)
        return best