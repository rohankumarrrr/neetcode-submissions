from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        maxHeap = [-v for k, v in freq.items()]
        heapq.heapify(maxHeap)

        stalled = deque()
        res = 0
        while maxHeap or stalled:
            res += 1
            if not maxHeap:
                res = stalled[-1][0]
            else:
                count = heapq.heappop(maxHeap)
                if count < -1:
                    stalled.appendleft((res + n, count + 1))
            if stalled and stalled[-1][0] == res:
                heapq.heappush(maxHeap, stalled.pop()[1])
        
        return res