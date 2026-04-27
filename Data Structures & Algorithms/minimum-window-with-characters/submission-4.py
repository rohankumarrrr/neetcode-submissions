class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        countS, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        resL, resLen = 0, float("inf")
        have, need = 0, len(countT)

        l, r = 0, 0
        while r < len(s):
            if s[r] in countT and countS.get(s[r], 0) + 1 == countT[s[r]]:
                have += 1
            
            countS[s[r]] = countS.get(s[r], 0) + 1
            r += 1

            while have == need:
                if r - l < resLen:
                    resL, resLen = l, r - l
                if s[l] in countT and not countS.get(s[l], 0) > countT.get(s[l], 0):
                    have -= 1
                countS[s[l]] = countS.get(s[l], 0) - 1
                l += 1
        
        return s[resL : resL + resLen] if not resLen == float("inf") else ""


        

