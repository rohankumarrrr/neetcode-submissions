class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        visited = {}

        def dfs(text1Idx, text2Idx):
            if text1Idx == len(text1) or text2Idx == len(text2):
                return 0
            if (text1Idx, text2Idx) in visited:
                return visited[(text1Idx, text2Idx)]
            if text1[text1Idx] == text2[text2Idx]:
                visited[(text1Idx, text2Idx)] = 1 + dfs(text1Idx + 1, text2Idx + 1)
            else:
                visited[(text1Idx, text2Idx)] = max(dfs(text1Idx + 1, text2Idx), dfs(text1Idx, text2Idx + 1))
            
            return visited[(text1Idx, text2Idx)]
        
        return dfs(0, 0)
        
