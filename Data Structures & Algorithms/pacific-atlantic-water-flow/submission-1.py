from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        pac = [(0, c) for c in range(cols)] + [(r, 0) for r in range(1, rows)]
        atl = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows-1)]

        def bfs(cells):
            queue, visited = deque(cells), set(cells)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        (0 <= nr < rows) and (0 <= nc < cols)
                        and heights[r][c] <= heights[nr][nc] and (nr, nc) not in visited
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return visited

        return [list(cell) for cell in bfs(pac).intersection(bfs(atl))]