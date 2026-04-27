from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in d:
                vec = [word for word in d[key]]
                vec.append(s)
                d[key] = vec
            else:
                d[key] = [s]
        
        return list(d.values())
            