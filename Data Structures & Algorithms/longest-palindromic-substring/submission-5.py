class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        memo = [[False] * len(s) for _ in range(len(s))]

        resI, resJ = 0, 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    if j - i > resJ - resI:
                        resI, resJ = i, j
        
        return s[resI:resJ + 1]