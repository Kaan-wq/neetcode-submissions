from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        border = (
            [(0, c) for c in range(cols) if board[0][c] == "O"]
            + [(r, 0) for r in range(1, rows-1) if board[r][0] == "O"]
            + [(rows-1, c) for c in range(cols) if board[rows-1][c] == "O"]
            + [(r, cols-1) for r in range(1, rows-1) if board[r][cols-1] == "O"]
        )

        def bfs(cells):
            queue, visited = deque(cells), set(cells)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        (0 <= nr < rows) and (0 <= nc < cols)
                        and (nr, nc) not in visited
                        and board[nr][nc] == "O"
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        visited = bfs(border)
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if not ((row, col) in visited):
                    board[row][col] = "X"