class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0]) if row_len > 0 else 0
        l, r = 0, row_len*col_len - 1
        while l <= r:
            m = (l + r) // 2
            v = matrix[m // col_len][m % col_len]
            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1
        return False