class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row * col - 1
        while lo <= hi:
            idx = (hi + lo) // 2
            idx_row = idx // col
            idx_col = idx % col

            if matrix[idx_row][idx_col] == target:
                return True
            elif matrix[idx_row][idx_col] > target:
                hi = idx - 1
            else:
                lo = idx + 1
        return False