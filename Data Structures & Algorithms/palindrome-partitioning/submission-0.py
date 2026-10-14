class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        result, state = [], []
        def backtrack(idx):
            if idx == length:
                result.append(state.copy())
                return
            for choice in range(idx+1, length+1):
                cut = s[idx:choice]
                if cut != cut[::-1]: continue

                state.append(cut)
                backtrack(choice)
                state.pop()

        backtrack(0)
        return result