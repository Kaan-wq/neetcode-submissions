class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(string, row, col):
            if string == word: return True
            if (
                not ((0 <= row < rows) and (0 <= col < cols))
                or board[row][col] == "#"
                or board[row][col] != word[len(string)]
            ): return False
            
            letter, board[row][col] = board[row][col], "#"

            result = (
                backtrack(string + letter, row - 1, col)
                or backtrack(string + letter, row + 1, col)
                or backtrack(string + letter, row, col - 1)
                or backtrack(string + letter, row, col + 1)
            )

            board[row][col] = letter

            return result

        for row in range(rows):
            for col in range(cols):
                if backtrack("", row, col): return True
        return False