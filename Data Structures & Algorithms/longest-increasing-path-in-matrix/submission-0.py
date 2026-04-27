class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # run a dfs from every starting point and return the maximum length
        # take maximum length from every starting point and return
        # O(n^2) * 4^(n^2)

        ROWS, COLS = len(matrix), len(matrix[0])

        memo = [[1] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if not memo[r][c] == 1:
                return memo[r][c]
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (not 0 <= nr < ROWS or
                    not 0 <= nc < COLS or
                    matrix[r][c] >= matrix[nr][nc]):

                    continue

                memo[r][c] = max(memo[r][c], 1 + dfs(nr, nc))
            
            return memo[r][c]
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res
            