class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                (r, c) in visited or
                not heights[r][c] >= prevHeight):

                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, -1)
            dfs(r, COLS - 1, atlantic, -1)
        for c in range(COLS):
            dfs(0, c, pacific, -1)
            dfs(ROWS - 1, c, atlantic, -1)
        
        res = []
        for (r, c) in pacific.intersection(atlantic):
            res.append([r, c])
        
        return res