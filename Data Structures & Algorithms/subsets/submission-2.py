class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(state, choices):
            result.append(state)
            
            for i, choice in enumerate(choices):
                backtrack(state + [choice], choices[i+1:])
        backtrack([], nums)
        return result
