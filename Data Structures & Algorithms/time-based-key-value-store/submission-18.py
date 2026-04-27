from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ""
        
        l, r = 0, len(self.timeMap[key]) - 1
        res = self.timeMap[key][0]

        while l <= r:
            m = l + (r - l) // 2
            if self.timeMap[key][m][0] <= timestamp and self.timeMap[key][m][0] >= res[0]:
                res = self.timeMap[key][m]
                l = m + 1
            else:
                r = m - 1
        
        return res[1]
                
