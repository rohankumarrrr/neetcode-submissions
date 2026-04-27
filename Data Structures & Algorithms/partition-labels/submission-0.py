class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        totalFreqCount = {}
        for c in s:
            totalFreqCount[c] = totalFreqCount.get(c, 0) + 1
        
        res = []

        currFreqCount = {}
        need = 0
        currStartIdx = 0
        for i in range(len(s)):
            c = s[i]
            if c not in currFreqCount:
                need += 1
            currFreqCount[c] = currFreqCount.get(c, 0) + 1
            if currFreqCount[c] == totalFreqCount[c]:
                need -= 1
            if need == 0:
                res.append(i - currStartIdx + 1)
                currFreqCount = {}
                currStartIdx = i + 1
        
        return res
            
            
