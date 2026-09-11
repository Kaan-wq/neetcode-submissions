class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        best = 0
        for n in nset:
            if (n - 1) not in nset:
                acc = 0
                while (n + acc) in nset:
                    acc += 1
                best = max(best, acc)
        return best