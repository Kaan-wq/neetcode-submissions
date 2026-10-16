class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int) -> bool:
            if (
            not (0 <= r < rows)
            or not (0 <= c < cols)
            or (r, c) in visited
            or grid[r][c] == "0"
            ):
                return False
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return True

        for row in range(rows):
            for col in range(cols):
                islands += dfs(row, col)

        return islands