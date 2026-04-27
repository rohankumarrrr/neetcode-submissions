class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(c for c in s.lower() if c.isalnum())
        left, right = 0, len(s_clean) - 1
        while left < right:
            if not s_clean[left] == s_clean[right]:
                return False
            left += 1
            right -= 1
        
        return True