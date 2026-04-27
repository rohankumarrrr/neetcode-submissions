class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        visited = {}

        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            visited[(i, j)] = 0

            for k in range(i, len(s)):
                if s[k] == t[j]:
                    visited[(i, j)] += dfs(k + 1, j + 1)
            
            return visited[(i, j)]
        
        return dfs(0, 0)
                