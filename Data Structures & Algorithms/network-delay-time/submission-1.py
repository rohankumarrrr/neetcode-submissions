import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = {u: [] for u in range(1, n + 1)}

        for u, v, w in times:
            edges[u].append((v, w))
        
        pq = [(0, k)] # (weight, vertex)
        visited = set()
    
        time = 0
        while pq:
            minWeight, u = heapq.heappop(pq)
            
            if u in visited:
                continue

            visited.add(u)

            time = minWeight

            for v, w in edges[u]:
                heapq.heappush(pq, (w + minWeight, v))
        
        return time if len(visited) == n else -1

                

