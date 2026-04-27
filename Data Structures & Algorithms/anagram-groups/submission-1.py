from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            if ''.join(sorted(word)) in d.keys():
                d[''.join(sorted(word))].append(word)
            else:
                d[''.join(sorted(word))] = [word]
        return list(d.values())