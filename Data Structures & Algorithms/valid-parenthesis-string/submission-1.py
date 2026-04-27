class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minOpened, maxOpened = 0, 0

        for c in s:
            if c == '(':
                minOpened, maxOpened = minOpened + 1, maxOpened + 1
            elif c == ')':
                minOpened, maxOpened = minOpened - 1, maxOpened - 1
            else:
                minOpened, maxOpened = minOpened - 1, maxOpened + 1
            
            if maxOpened < 0:
                return False
            if minOpened < 0:
                minOpened = 0
        
        return minOpened == 0
