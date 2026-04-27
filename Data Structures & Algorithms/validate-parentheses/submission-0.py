class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stck = []
        for c in s:
            if c not in mp:
                stck.append(c)
            elif not stck or stck.pop() != mp[c]:
                return False
        
        return not stck
        
