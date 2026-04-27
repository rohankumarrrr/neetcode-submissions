class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        visited = {}

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n:
                return 0
            if (r, c) in visited:
                return visited[(r, c)]

            visited[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return visited[(r, c)]
        
        return dfs(0, 0)