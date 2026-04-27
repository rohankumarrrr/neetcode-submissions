import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5

        maxHeap = []
        for point in points:
            maxHeap.append([-distance(point), point])
        
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        return [elem[1] for elem in maxHeap]

