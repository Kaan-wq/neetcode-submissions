class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, state = [], []

        def backtrack(total, choices):
            if total == target:
                result.append(state.copy())
                return

            for i, choice in enumerate(choices):
                if i > 0 and choice == choices[i-1]: continue
                if total + choice > target: return

                state.append(choice)
                backtrack(total + choice, choices[i+1:])
                state.pop()

        backtrack(0, candidates)
        return result