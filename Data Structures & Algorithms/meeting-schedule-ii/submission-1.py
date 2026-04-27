"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        startTimes, endTimes = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])

        startIdx, endIdx = 0, 0

        maxOverlap, currUsed = 0, 0

        while startIdx < len(intervals):
            if startTimes[startIdx] < endTimes[endIdx]:
                currUsed += 1
                maxOverlap = max(maxOverlap, currUsed)
                startIdx += 1
            else:
                currUsed -= 1
                endIdx += 1
        
        return maxOverlap