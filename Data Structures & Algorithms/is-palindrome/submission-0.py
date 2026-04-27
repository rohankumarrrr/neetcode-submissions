class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join(char for char in s if char.isalnum())
        clean_str = clean_str.lower()
        for i in range(0, int(len(clean_str) / 2)):
            if (clean_str[i] != clean_str[len(clean_str) - 1 - i]):
                return False
        return True