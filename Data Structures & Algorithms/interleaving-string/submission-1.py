class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        visited = {} # (i, j)

        def dfs(s1Idx, s2Idx):
            s3Idx = s1Idx + s2Idx
            if s3Idx == len(s3):
                return (s1Idx == len(s1) and s2Idx == len(s2))
            
            if (s1Idx, s2Idx) in visited:
                return visited[(s1Idx, s2Idx)]
            
            flag = False
            if s1Idx < len(s1) and s1[s1Idx] == s3[s3Idx]:
                flag = flag or dfs(s1Idx + 1, s2Idx)
            if s2Idx < len(s2) and s2[s2Idx] == s3[s3Idx]:
                flag = flag or dfs(s1Idx, s2Idx + 1)
            
            visited[(s1Idx, s2Idx)] = flag
            return visited[(s1Idx, s2Idx)]
        
        return dfs(0, 0)
