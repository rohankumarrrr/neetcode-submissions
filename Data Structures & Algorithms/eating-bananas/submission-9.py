import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = l + (r - l) // 2
            minH = sum([math.ceil(float(pile) / m) for pile in piles])
            if minH <= h:
                r = m - 1
                k = m
            else:
                l = m + 1

        return k