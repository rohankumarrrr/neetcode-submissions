class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        for c in s:
            if not c in closeToOpen:
                stack.append(c)
            elif stack and closeToOpen[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack