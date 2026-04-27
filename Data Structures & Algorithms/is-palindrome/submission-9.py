class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlNum(c):
            return (ord('a') <= ord(c) <= ord('z')
                or ord('A') <= ord(c) <= ord('Z')
                or ord('0') == ord(c)
                or ord ('1') <= ord(c) <= ord('9'))
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isAlNum(s[l]):
                l += 1
            while l < r and not isAlNum(s[r]):
                r -= 1
            
            if not s[l].lower() == s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True