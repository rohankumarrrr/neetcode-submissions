class MedianFinder:

    def __init__(self):
        self.first = []
        self.second = []

    def addNum(self, num: int) -> None:
        if not self.second or num > self.second[0]:
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
        if len(self.second) - len(self.first) > 1:
            tmp = self.second[0]
            heapq.heappop(self.second)
            heapq.heappush(self.first, -tmp)
        elif len(self.first) - len(self.second) > 1:
            tmp = -self.first[0]
            heapq.heappop(self.first)
            heapq.heappush(self.second, tmp)

    def findMedian(self) -> float:
        if (len(self.first) + len(self.second)) % 2 == 0:
            return (-self.first[0] + self.second[0]) / 2
        if len(self.first) > len(self.second):
            return -self.first[0]
        return self.second[0]
        