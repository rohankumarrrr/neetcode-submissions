class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        minRemovals = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                minRemovals += 1
                prevEnd = min(end, prevEnd)
        
        return minRemovals
