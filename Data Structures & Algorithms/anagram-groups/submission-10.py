from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        vals = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1 
            key = tuple(freq)
            vals[key].append(s)
        
        return [v for k, v in vals.items()]
        
