class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                (r, c) in visited or
                grid[r][c] == "0"):

                return False
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return True

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    res += 1
        
        return res

        


