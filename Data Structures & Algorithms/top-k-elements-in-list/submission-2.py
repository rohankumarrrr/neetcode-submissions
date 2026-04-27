from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = Counter(nums)
        k_most = sorted(c.values())
        vals = set(k_most[len(k_most) - k:])
        for n in c.keys():
            if c[n] in vals:
                res.append(n)
        return res
