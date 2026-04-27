import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjList = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        
        minCost = 0
        seen = set()
        pq = []
        heapq.heappush(pq, (0, 0))

        while pq and len(seen) < len(points):
            cost, pt = heapq.heappop(pq)
            
            if pt in seen:
                continue
                
            minCost += cost
            seen.add(pt)

            for nextCost, nextPt in adjList[pt]:
                if nextPt in seen:
                    continue
                heapq.heappush(pq, (nextCost, nextPt))
                    
        
        return minCost
            




