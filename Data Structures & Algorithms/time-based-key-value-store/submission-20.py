from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.timeMap or timestamp < self.timeMap[key][0][0]:
            return ""

        nums = self.timeMap[key]
        l, r = 0, len(nums) - 1
        bestTimestamp = 0

        while l <= r:
            m = l + (r - l) // 2
            if nums[m][0] <= timestamp:
                bestTimestamp = m
                l = m + 1
            else:
                r = m - 1
        
        return nums[bestTimestamp][1]
