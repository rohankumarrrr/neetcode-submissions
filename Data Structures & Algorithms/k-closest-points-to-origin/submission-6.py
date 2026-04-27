class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        vals = [[getDistance(point), point] for point in points]

        def quickSelect(l, r):
            pivot, p = vals[r], l
            for i in range(l, r):
                if vals[i][0] <= pivot[0]:
                    vals[i], vals[p] = vals[p], vals[i]
                    p += 1
            vals[r], vals[p] = vals[p], vals[r]
            if p > k - 1:
                return quickSelect(l, p - 1)
            if p < k - 1:
                return quickSelect(p + 1, r)
            return p
        
        return [point for _, point in vals[:quickSelect(0, len(points) - 1) + 1]]