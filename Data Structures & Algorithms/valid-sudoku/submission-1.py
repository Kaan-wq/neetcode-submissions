class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)

        rset = [set() for _ in range(size)]
        cset = [set() for _ in range(size)]
        gset = [set() for _ in range(size)]

        for i, r in enumerate(board):
            for j, c in enumerate(board[i]):
                if c != ".":
                    gidx = (i // 3) * 3 + j // 3
                    if c in rset[i] or c in cset[j] or c in gset[gidx]: return False
                    rset[i].add(c)
                    cset[j].add(c)
                    gset[gidx].add(c)
        return True