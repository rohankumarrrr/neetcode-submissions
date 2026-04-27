from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.timeMap[key]

        if not nums or timestamp < nums[0][0]:
            return ""

        resI = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m][0] <= timestamp:
                resI = m
                l = m + 1
            else:
                r = m - 1
        
        return nums[resI][1]
        
        
