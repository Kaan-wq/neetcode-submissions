class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [nums[0]]
        right = [nums[-1]]

        for i in range(1, n):
            left.append(left[i - 1] * nums[i])
            right.append(right[i - 1] * nums[-i - 1])
        
        right.reverse()
        output = []
        for i in range(0, n):
            l = left[i-1] if i > 0 else 1
            r = right[i + 1] if i < n - 1 else 1
            output.append(l * r)
        return output
        