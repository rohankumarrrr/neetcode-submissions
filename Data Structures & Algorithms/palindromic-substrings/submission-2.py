class Solution:
    def countSubstrings(self, s: str) -> int:
        
        memo = [[False] * len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j - i < 2 and s[i] == s[j]:
                    memo[i][j] = True
                elif memo[i + 1][j - 1] and s[i] == s[j]:
                    memo[i][j] = True
                if memo[i][j]:
                    res += 1
        
        return res