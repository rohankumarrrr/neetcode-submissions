from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        heap = []
        for num in c.keys():
            heapq.heappush(heap, (c[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
