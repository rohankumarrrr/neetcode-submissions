"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s = e = 0
        currUsed = 0
        maxOverlap = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                currUsed += 1
                maxOverlap = max(maxOverlap, currUsed)
                s += 1
            else:
                currUsed -= 1
                e += 1
        
        return maxOverlap