class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            newStart, newEnd = newInterval

            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart > end:
                res.append(intervals[i])
            else:
                newInterval = [min(start, newStart), max(end, newEnd)]
        
        res.append(newInterval)

        return res

