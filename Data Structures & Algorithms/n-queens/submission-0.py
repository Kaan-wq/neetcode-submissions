class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n] * n
        cols, diagl, diagr = set(), set(), set()
        result = []
        def backtrack(row, col, queens):
            if (
                col in cols
                or (row + col) in diagl
                or (row - col) in diagr
            ): return

            board[row] = ("." * (col)) + "Q" + ("." * (n-col-1))

            if queens == n - 1:
                result.append(board.copy())
                board[row] = "." * n
                return

            cols.add(col)
            diagl.add(row + col)
            diagr.add(row - col)

            for c in range(n):
                backtrack(row+1, c, queens+1)

            board[row] = "." * n
            cols.remove(col)
            diagl.remove(row + col)
            diagr.remove(row - col)
            
        for c in range(n):
            backtrack(0, c, 0)
        return result