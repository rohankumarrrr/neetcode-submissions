class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        maxHeap = []
        for point in points:
            distance = getDistance(point)
            heapq.heappush(maxHeap, [-distance, point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for _, point in maxHeap]