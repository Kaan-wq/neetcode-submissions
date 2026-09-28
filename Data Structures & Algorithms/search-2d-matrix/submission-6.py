class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row * col - 1
        while lo <= hi:
            idx = (hi + lo) // 2
            val = matrix[idx // col][idx % col]

            if val == target:
                return True
            elif val > target:
                hi = idx - 1
            else:
                lo = idx + 1
        return False