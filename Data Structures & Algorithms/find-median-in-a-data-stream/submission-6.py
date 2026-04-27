class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def addNum(self, num: int) -> None:
        if self.second and self.second[0] < num:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        
        if abs(len(self.first) - len(self.second)) > 1:
            a, b = self.first, self.second
            if len(self.first) > len(self.second):
                a, b = b, a
            heapq.heappush(a, -heapq.heappop(b))

    def findMedian(self) -> float:
        if len(self.first) > len(self.second):
            return -self.first[0]
        if len(self.first) < len(self.second):
            return self.second[0]
        
        return (-self.first[0] + self.second[0]) / 2
        