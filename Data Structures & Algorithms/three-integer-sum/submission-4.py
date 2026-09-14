class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solutions = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                val_i, val_l, val_r = nums[i], nums[l], nums[r]
                val_sum = val_i + val_l + val_r
                if val_sum == 0:
                    solutions.append([val_i, val_l, val_r])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif val_sum < 0:
                    l += 1
                else:
                    r -= 1
        print(solutions)
        return solutions