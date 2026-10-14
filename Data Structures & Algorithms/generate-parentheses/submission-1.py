class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, state = [], []
        choices = (["("] * n) + ([")"] * n)

        def backtrack(string, order):
            if len(state) == 2 * n:
                result.append(string)
                return
            
            for i, choice in enumerate(choices):
                if (
                    choice is None 
                    or (i > 0 and choice == choices[i-1])
                    or (order == 0 and choice == ")")
                ): continue

                state.append(choice)
                chosen, choices[i] = choices[i], None
                order = order + (1 if chosen == "(" else -1)

                backtrack(string + chosen, order)

                state.pop()
                choices[i] = chosen
                order = order + (-1 if chosen == "(" else 1)
        
        backtrack("", 0)
        return result