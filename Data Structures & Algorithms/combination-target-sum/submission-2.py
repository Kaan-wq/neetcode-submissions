class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(state, choices):
            total = sum(state)
            if total == target:
                result.append(state)
                return
            if total > target: return
            
            for i, choice in enumerate(choices):
                new_state = state + [choice]
                backtrack(new_state, choices[i:])
        backtrack([], nums)
        return result