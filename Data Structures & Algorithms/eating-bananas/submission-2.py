class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        k = 0
        while min_speed <= max_speed:
            speed = min_speed + (max_speed - min_speed) // 2
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / speed)
            if hours_needed <= h:
                max_speed = speed -1
                k = speed
            else:
                min_speed = speed + 1
        return k