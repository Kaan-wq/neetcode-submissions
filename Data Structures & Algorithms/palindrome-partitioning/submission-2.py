class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, state, length = [], [], len(s)
        def backtrack(idx):
            # print(idx)
            if idx == length:
                result.append(state.copy())
                return
            
            for i in range(idx+1, length+1):
                choice = s[idx:i]
                if choice != choice[::-1]: continue
                state.append(choice)
                backtrack(i)
                state.pop()
        backtrack(0)
        return result