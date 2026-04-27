class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()
        for x in nums:
            if x in hset:
                return x
            else:
                hset.add(x)
        
        return -1