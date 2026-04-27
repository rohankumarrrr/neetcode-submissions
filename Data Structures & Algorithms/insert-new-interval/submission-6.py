class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newIntervalInserted = False
        for i in range(len(intervals)):
            start, end = intervals[i]
            if newInterval[0] < start:
                intervals.insert(i, newInterval)
                newIntervalInserted = True
                break
        
        if not newIntervalInserted:
            intervals.append(newInterval)

        res = []

        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]
            else:
                res.append([start, end])
        
        return res
            