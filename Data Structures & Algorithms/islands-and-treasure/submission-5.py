class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            visited = set()
            q.appendleft((r, c))
            dist = 0
            while q:
                for i in range(len(q)):
                    row, col = q.pop()
                    if (not row in range(ROWS) or
                        not col in range(COLS) or
                        (row, col) in visited or
                        grid[row][col] == -1):
                        
                        continue

                    if grid[row][col] == 0:
                        return dist
                    
                    visited.add((row, col))
                    for dr, dc in STEPS:
                        q.appendleft((row + dr, col + dc))

                dist += 1
            
            return INF
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)


                    
