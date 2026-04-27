from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        pq = [(0, k)]
        visited = set()
        time = 0

        while pq:
            initWeight, initNode = heapq.heappop(pq)
            if initNode in visited:
                continue
            visited.add(initNode)

            time = initWeight

            for nextNode, nextWeight in edges[initNode]:
                if nextNode not in visited:
                    heapq.heappush(pq, (initWeight + nextWeight, nextNode))
        
        return time if len(visited) == n else -1