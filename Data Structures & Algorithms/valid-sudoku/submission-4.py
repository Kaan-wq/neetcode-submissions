class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        g = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, el in enumerate(row):
                if el == ".":
                    continue

                g_idx = (i // 3) * 3 + (j // 3)
                if (el in r[i]) or (el in c[j]) or (el in g[g_idx]):
                    return False

                r[i].add(el)
                c[j].add(el)
                g[g_idx].add(el)
        return True