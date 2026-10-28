CHEST, LAND, WATER = 0, 2147483647, -1
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque(
            (r, c) for r in range(rows)
            for c in range(cols) if grid[r][c] == 0
        )

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == LAND:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))