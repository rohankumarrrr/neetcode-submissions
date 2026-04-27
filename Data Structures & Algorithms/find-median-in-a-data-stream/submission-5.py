class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def addNum(self, num: int) -> None:
        if self.second and num < self.second[0]:
            heapq.heappush(self.first, -num)
        else:
            heapq.heappush(self.second, num)

        if abs(len(self.first) - len(self.second)) > 1:
            a, b = self.first, self.second
            if len(a) > len(b):
                a, b = b, a
            val = heapq.heappop(b)
            heapq.heappush(a, -val)

    def findMedian(self) -> float:
        if len(self.first) == len(self.second):
            return (-self.first[0] + self.second[0]) / 2
        if len(self.first) > len(self.second):
            return -self.first[0]
        return self.second[0]
        