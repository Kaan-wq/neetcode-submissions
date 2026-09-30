class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] + nums
        r = nums + [1]

        for i in range(n):
            l[i+1] = l[i] * nums[i]
        for i in reversed(range(n-1)):
            r[i] = r[i + 1] * nums[i]
        
        res = []
        for i in range(1, n+1):
            res.append(l[i - 1] * r[i])
        return res
