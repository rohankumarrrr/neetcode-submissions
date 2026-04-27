class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        fresh, q = 0, deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        time = 0
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.pop()

                for dr, dc in steps:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.appendleft((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1

