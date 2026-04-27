class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stck = []
        for c in s:
            if c in d.keys():
                if stck and d[c] == stck[-1]:
                    stck.pop()
                else:
                    return False
            else:
                stck.append(c)
        
        return not stck
        
