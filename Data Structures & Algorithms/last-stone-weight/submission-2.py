class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones) > 1):
            sorted_stones = sorted(stones, reverse=True)
            heavy1 = sorted_stones[0]
            heavy2 = sorted_stones[1]
            if (heavy1 == heavy2):
                stones.remove(heavy1)
                stones.remove(heavy2)
            elif (heavy2 < heavy1):
                stones.remove(heavy2)
                stones[stones.index(heavy1)] = heavy1 - heavy2
        stones.append(0)
        return stones[0]