class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxLen = 1
        l, r = 0, 1
        chars = set()
        chars.add(s[l])
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            r += 1

            maxLen = max(r - l, maxLen)
        
        return maxLen

