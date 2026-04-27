class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, v in count.items():
            buckets[v - 1].append(n)
        
        res = []
        for bucket in buckets[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res

        return res 