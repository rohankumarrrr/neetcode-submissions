class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                (r, c) in visited or
                grid[r][c] == 0):

                return 0
            
            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea