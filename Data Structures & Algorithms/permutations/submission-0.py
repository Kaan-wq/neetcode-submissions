class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, state = [], []
        def backtrack(choices):
            if len(state) == len(nums):
                result.append(state.copy())
                return
            
            for i, choice in enumerate(choices):
                if choice is None: continue

                state.append(choice)
                value, choices[i] = choices[i], None

                backtrack(choices)

                state.pop()
                choices[i] = value
        backtrack(nums)
        return result