class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [False] * (len(s) + 1)
        memo[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    memo[i] = memo[i] or memo[i+len(word)]
        
        return memo[0]