from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        vals = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            vals[key].append(s)
        
        return [v for k, v in vals.items()]
        
