class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        freshCnt = 0
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshCnt += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        time = 0
        while q and freshCnt > 0:
            for _ in range(len(q)):
                r, c = q.pop()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        (nr, nc) in visited or
                        not grid[nr][nc] == 1):

                        continue
                    
                    grid[nr][nc] = 2
                    freshCnt -= 1

                    q.appendleft((nr, nc))
                    visited.add((nr, nc))
            time += 1

        return time if freshCnt == 0 else -1