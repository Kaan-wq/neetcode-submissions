class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result, state = False, []
        rows, cols = len(board), len(board[0])

        def backtrack(string, row, col):
            nonlocal result
            # print(f"WORD {word} | STRING {string} ROW {row} COL {col}")
            if string == word:
                result = True
                return
            if (
                not ((0 <= row < rows) and (0 <= col < cols))
                or len(state) == len(word)
                or board[row][col] == "#"
            ): return
            
            letter, board[row][col] = board[row][col], "#"
            state.append(letter)

            backtrack(string + letter, row - 1, col)
            backtrack(string + letter, row + 1, col)
            backtrack(string + letter, row, col - 1)
            backtrack(string + letter, row, col + 1)

            board[row][col] = letter
            state.pop()

        for row in range(rows):
            for col in range(cols):
                backtrack("", row, col)
        return result