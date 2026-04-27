class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        # [1, 3], [2, 3]

        intervalIdx = 0

        res = {}

        minHeap = []
        
        for q in sorted(queries):
            while intervalIdx < len(intervals) and intervals[intervalIdx][0] <= q:
                start, end = intervals[intervalIdx]
                heapq.heappush(minHeap, (end - start + 1, end))
                intervalIdx += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

