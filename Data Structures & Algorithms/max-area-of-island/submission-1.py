class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> int:
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            local_area = 1
            for dr, dc in directions:
                local_area += dfs(r + dr, c + dc)

            return local_area
        
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area