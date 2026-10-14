class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n] * n
        cols, diagl, diagr = set(), set(), set()
        result = []
        def backtrack(row):
            if row == n:
                result.append(board.copy())
                return

            for col in range(n):
                if (
                    col in cols
                    or (row + col) in diagl
                    or (row - col) in diagr
                ): continue

                board[row] = ("." * (col)) + "Q" + ("." * (n-col-1))
                cols.add(col)
                diagl.add(row + col)
                diagr.add(row - col)

                backtrack(row+1)

                board[row] = "." * n
                cols.remove(col)
                diagl.remove(row + col)
                diagr.remove(row - col)
            
        backtrack(0)
        return result