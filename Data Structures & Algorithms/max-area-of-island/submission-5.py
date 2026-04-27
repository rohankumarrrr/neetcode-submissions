class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                not grid[r][c] == 1):

                return 0
            
            grid[r][c] = 0

            return 1 + (
                dfs(r + 1, c) +
                dfs(r - 1, c) + 
                dfs(r, c + 1) + 
                dfs(r, c - 1)
            )
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(dfs(r, c), maxArea)
        
        return maxArea