class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            visited = set()
            dist = 0
            q.appendleft((r, c))
            while q:
                for _ in range(len(q)):
                    row, col = q.pop()
                    if (not row in range(ROWS) or
                        not col in range(COLS) or
                        (row, col) in visited or
                        grid[row][col] == -1):

                        continue

                    visited.add((row, col))
                    if grid[row][col] == 0:
                        return dist
                    
                    for dr, dc in DIRECTIONS:
                        nr, nc = row + dr, col + dc
                        q.appendleft((nr, nc))
                dist += 1
            
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
