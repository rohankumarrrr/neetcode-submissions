class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.pop()
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (not nr in range(ROWS) or
                        not nc in range(COLS) or
                        not grid[nr][nc] == 1):

                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.appendleft((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1


