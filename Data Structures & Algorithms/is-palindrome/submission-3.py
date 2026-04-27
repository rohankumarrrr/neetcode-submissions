class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left >= right:
                break
            if not s[left] == s[right]:
                return False
            left += 1
            right -= 1
        return True
            