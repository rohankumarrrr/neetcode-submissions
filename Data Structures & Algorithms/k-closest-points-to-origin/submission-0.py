import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5

        distances_to_point = defaultdict(list)
        for point in points:
            distances_to_point[distance(point)].append(point)
        
        distances = list(distances_to_point.keys())
        heapq.heapify(distances)

        res = []
        i = 0
        while i < k:
            points_list = distances_to_point[heapq.heappop(distances)]
            while i < k and points_list:
                res.append(points_list[-1])
                points_list.pop()
                i += 1
        
        return res
