class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            q = deque()
            q.appendleft((r, c))
            
            visited = set()
            dist = 0
            while q:
                for i in range(len(q)):
                    row, col = q.pop()
                    if not 0 <= row < ROWS or not 0 <= col < COLS or (row, col) in visited or grid[row][col] == -1:
                        continue
                    
                    if grid[row][col] == 0:
                        return dist

                    visited.add((row, col))
                    q.appendleft((row + 1, col))
                    q.appendleft((row - 1, col))
                    q.appendleft((row, col + 1))
                    q.appendleft((row, col - 1))
                dist += 1
            
            return INF
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
