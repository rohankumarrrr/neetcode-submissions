class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resIdx, resLen = 0, 0
        memo = [[False] * len(s) for _ in range(len(s))]
        
        # memo[i][j] is the length of the longest palindrome considering 

        for i in range(len(s) - 1, -1, -1):
            memo[i][i] = True
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1]):
                    memo[i][j] = True
                    if resLen < (j - i + 1):
                        resLen = j - i + 1
                        resIdx = i
        
        return s[resIdx:resIdx + resLen]
            