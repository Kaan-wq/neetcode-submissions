class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, state = [], []
        def backtrack(state, total, choices):
            if total == target:
                result.append(state.copy())
                return
            if total > target: return
            
            for i, choice in enumerate(choices):
                state.append(choice)
                backtrack(state, total + choice, choices[i:])
                state.pop()
        backtrack([], 0, nums)
        return result