from collections import Counter
from itertools import islice
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = dict(islice(sorted(freq.items(), key=lambda item: item[1], reverse=True), k))
        return list(res.keys())