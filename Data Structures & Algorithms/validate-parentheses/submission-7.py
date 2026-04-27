class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for c in s:
            if not c in mp:
                stack.append(c)
            elif stack and stack[-1] == mp[c]:
                stack.pop()
            else:
                return False
        
        return not stack