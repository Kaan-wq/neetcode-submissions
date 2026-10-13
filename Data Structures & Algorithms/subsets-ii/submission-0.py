class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, state = [], []

        def backtrack(choices):
            result.append(state.copy())

            for i, choice in enumerate(choices):
                if i > 0 and choice == choices[i-1]: continue
                state.append(choice)
                backtrack(choices[i+1:])
                state.pop()
        
        backtrack(nums)
        return result