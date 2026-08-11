class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        n = len(s_nums)
        sols = []
        for i in range(n - 2):
            val_i = s_nums[i]
            if i > 0 and val_i == s_nums[i - 1]: continue
            l = i + 1
            r = n - 1
            while l < r:
                val_l = s_nums[l]
                val_r = s_nums[r]
                val = val_i + val_l + val_r
                if val == 0:
                    sols.append([val_i, val_l, val_r])
                    l += 1
                    r -= 1
                    while l < r and s_nums[l] == s_nums[l - 1]:
                        l += 1
                elif val > 0:
                    r -= 1
                else: 
                    l += 1
        return sols