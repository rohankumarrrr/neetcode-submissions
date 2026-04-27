class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                not grid[r][c] == "1"):

                return 0
            
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return 1
        
        numIslands = 0
        for r in range(ROWS):
            for c in range(COLS):
                numIslands += dfs(r, c)
        
        return numIslands