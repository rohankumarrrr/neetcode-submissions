class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqS = {}
        for c in s:
            freqS[c] = freqS.get(c, 0) + 1
        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        return freqS == freqT