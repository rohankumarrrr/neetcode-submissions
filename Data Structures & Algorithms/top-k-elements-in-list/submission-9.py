class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        res = []

        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []