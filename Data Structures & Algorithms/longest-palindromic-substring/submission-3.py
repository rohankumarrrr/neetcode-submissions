class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        memo = [[False for i in range(len(s))] for i in range(len(s))]
        resI, resJ = 0, 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j - i < 2 and s[i] == s[j]:
                    memo[i][j] = True
                elif s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True
                if memo[i][j] and j - i > resJ - resI:
                    resI, resJ = i, j
        
        return s[resI:resJ+1]