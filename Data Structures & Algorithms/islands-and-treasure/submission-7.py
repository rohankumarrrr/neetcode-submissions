from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.appendleft((r, c))
                    visited.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.pop()

                grid[r][c] = dist

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        (nr, nc) in visited or
                        grid[nr][nc] == -1):

                        continue
                    
                    q.appendleft((nr, nc))
                    visited.add((nr, nc))
            dist += 1