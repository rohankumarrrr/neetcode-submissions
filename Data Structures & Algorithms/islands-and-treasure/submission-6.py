from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.appendleft((r, c))
        
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.pop()
                for dr, dc in STEPS:
                    nr, nc = r + dr, c + dc
                    if (not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        not grid[nr][nc] == INF):

                        continue
                    
                    grid[nr][nc] = dist

                    q.appendleft((nr, nc))
            
            dist += 1
