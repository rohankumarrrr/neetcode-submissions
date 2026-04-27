class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        pre = ""
        length = min(len(s) for s in strs)
        for i in range(length):
            for s in strs:
                if not s[i] == strs[0][i]:
                    return pre
            pre += strs[0][i]
        
        return pre