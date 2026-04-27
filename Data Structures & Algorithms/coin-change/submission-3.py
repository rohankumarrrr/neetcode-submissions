from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        q = deque()
        visited = set()

        q.appendleft(0)
        visited.add(0)

        dist = 0
        while q:
            for _ in range(len(q)):
                currAmount = q.pop()
                if currAmount == amount:
                    return dist
                for c in coins:
                    if (currAmount + c > amount or
                        currAmount + c in visited):
                        continue
                    q.appendleft(currAmount + c)
                    visited.add(currAmount + c)
            dist += 1
        
        return -1