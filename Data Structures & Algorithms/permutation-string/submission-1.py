class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_hmap = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            substr = s2[i:i+len(s1)]
            s2_hmap = Counter(substr)
            if s1_hmap == s2_hmap:
                return True
        
        return False