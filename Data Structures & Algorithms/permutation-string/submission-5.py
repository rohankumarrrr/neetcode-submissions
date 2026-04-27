class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        chars1, chars2 = [0] * 26, [0] * 26
        l, r = 0, len(s1)

        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1
        
        while r < len(s2):
            if chars1 == chars2:
                return True
            chars2[ord(s2[l]) - ord('a')] -= 1
            chars2[ord(s2[r]) - ord('a')] += 1
            l, r = l + 1, r + 1
        
        return chars1 == chars2