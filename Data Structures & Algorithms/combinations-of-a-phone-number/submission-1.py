class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        sequence = [mapping[digit] for digit in digits]
        result, state = [], []

        def backtrack(row):
            if row == len(digits):
                result.append("".join(state))
                return
            
            for letter in sequence[row]:
                state.append(letter)
                backtrack(row+1)
                state.pop()
        
        backtrack(0)
        return result