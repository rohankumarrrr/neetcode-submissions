from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k in d:
            if d[k] == 1:
                return k
        return 0