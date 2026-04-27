class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for c in s:
            if not c in mp:
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == mp[c]:
                stack.pop()
            else:
                return False
        
        return not stack