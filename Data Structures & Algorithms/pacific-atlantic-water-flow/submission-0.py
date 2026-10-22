from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue_pac = deque([(0, c) for c in range(cols)]+[(r, 0) for r in range(1, rows)])
        queue_atl = deque([(rows-1, c) for c in range(cols)]+[(r, cols-1) for r in range(rows-1)])

        res_pac, vis_pac = [], set(queue_pac)
        while queue_pac:
            r, c = queue_pac.popleft()
            if r == rows-1 or c == cols-1: res_pac.append([r, c])
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    (0 <= nr < rows) and (0 <= nc < cols)
                    and heights[r][c] <= heights[nr][nc] and (nr, nc) not in vis_pac
                ):
                    queue_pac.append((nr, nc))
                    vis_pac.add((nr, nc))

        res_atl, vis_atl = [], set(queue_atl)
        while queue_atl:
            r, c = queue_atl.popleft()
            if r == 0 or c == 0: res_atl.append([r, c])
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    (0 <= nr < rows) and (0 <= nc < cols)
                    and heights[r][c] <= heights[nr][nc] and (nr, nc) not in vis_atl
                ):
                    queue_atl.append((nr, nc))
                    vis_atl.add((nr, nc))

        return [list(cell) for cell in vis_pac.intersection(vis_atl)]