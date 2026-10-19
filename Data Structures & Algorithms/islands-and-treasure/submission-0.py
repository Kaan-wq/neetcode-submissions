CHEST, LAND, WATER = 0, 2147483647, -1
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque(
            [
                (0, row, col) for row in range(rows)
                for col in range(cols) if grid[row][col] == CHEST
            ]
        )

        while queue:
            d, r, c = queue.popleft()
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or grid[r][c] == WATER
                or (d != 0 and grid[r][c] != LAND)
            ): continue

            grid[r][c] = d
            for dr, dc in directions:
                queue.append((d+1, r+dr, c+dc))