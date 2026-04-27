class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        print(counter)
        for n, count in counter.items():
            buckets[count - 1].append(n)
        
        res = []
        for bucket in buckets[::-1]:
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
                