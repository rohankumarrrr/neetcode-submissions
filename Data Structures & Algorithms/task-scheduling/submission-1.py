from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        
        maxHeap = [-v for k, v in freq.items()]
        heapq.heapify(maxHeap)
        
        res = 0
        stalled = deque()
        while maxHeap or stalled:
            res += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                if count < -1:
                    stalled.appendleft((res + n, count + 1))
            if stalled and stalled[-1][0] == res:
                heapq.heappush(maxHeap, stalled.pop()[1])
        
        return res