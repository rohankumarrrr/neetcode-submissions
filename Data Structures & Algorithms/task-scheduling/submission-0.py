from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(maxHeap)
        
        res = 0
        stalled = deque()
        while maxHeap or stalled:
            res += 1
            if maxHeap:
                quantity, task = heapq.heappop(maxHeap)
                if quantity < -1:
                    stalled.appendleft((res + n, (quantity + 1, task)))
            if stalled and stalled[-1][0] == res:
                heapq.heappush(maxHeap, stalled.pop()[1])
        
        return res