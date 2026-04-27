class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def addNum(self, num: int) -> None:

        if not self.second or num > self.second[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        
        a, b = self.first, self.second
        if len(a) > len(b):
            a, b = b, a
        if len(b) - len(a) > 1:
            tmp = b[0]
            heapq.heappop(b)
            heapq.heappush(a, -tmp)

    def findMedian(self) -> float:
        if (len(self.first) + len(self.second)) % 2 == 0:
            return (-self.first[0] + self.second[0]) / 2
        if len(self.first) > len(self.second):
            return -self.first[0]
        return self.second[0]
        