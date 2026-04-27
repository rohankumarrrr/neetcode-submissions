class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        freshCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCount += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        time = 0
        while q and freshCount > 0:
            for i in range(len(q)):
                r, c = q.pop()
                for dr, dc in STEPS:
                    nr, nc = r + dr, c + dc
                    if (not nr in range(ROWS) or
                        not nc in range(COLS) or
                        not grid[nr][nc] == 1):
                        continue

                    grid[nr][nc] = 2
                    freshCount -= 1
                    q.appendleft((nr, nc))

            time += 1
        
        return time if freshCount == 0 else -1
