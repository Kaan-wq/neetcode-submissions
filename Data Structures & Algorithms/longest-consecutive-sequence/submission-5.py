class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        for n in nset:
            acc = 0
            if (n - 1) in nset:
                continue
            g = n
            while g in nset:
                acc += 1
                g +=1
            res = max(res, acc)
        return res 