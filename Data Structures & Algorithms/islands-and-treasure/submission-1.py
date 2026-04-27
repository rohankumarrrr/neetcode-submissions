from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def bfs(r, c):
            q = deque()
            q.appendleft((r, c))
            visited = set()
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.pop()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (not 0 <= nr < ROWS or
                            not 0 <= nc < COLS or
                            (nr, nc) in visited or
                            grid[nr][nc] == -1):

                            continue

                        visited.add((nr, nc))
                        q.appendleft((nr, nc))
                steps += 1
            
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)