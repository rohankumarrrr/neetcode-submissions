class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        handCount = {}
        for x in hand:
            handCount[x] = handCount.get(x, 0) + 1

        while handCount:
            x = max(key for key, val in handCount.items())
            size = 0
            
            while x in handCount and size < groupSize:
                size += 1
                handCount[x] -= 1
                if handCount[x] == 0:
                    del handCount[x]
                x -= 1
            
            if not size == groupSize:
                return False
        
        return not handCount