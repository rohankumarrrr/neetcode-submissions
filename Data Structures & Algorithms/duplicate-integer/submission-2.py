class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Pick ith element, loop from i to end to find equal
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False