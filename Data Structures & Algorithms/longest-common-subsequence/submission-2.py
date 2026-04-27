class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # memo[i][j] represents the length of the longest common subsequence 
        # considering text1[0...i] and text2[0...j]

        visited = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in visited:
                return visited[(i, j)]
            if text1[i] == text2[j]:
                visited[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                visited[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return visited[(i, j)]
        
        return dfs(0, 0)

