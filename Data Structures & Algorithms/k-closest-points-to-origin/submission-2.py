class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        maxHeap = [[-getDistance(point), point] for point in points]
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        return [point for _, point in maxHeap]