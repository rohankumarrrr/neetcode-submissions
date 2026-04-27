class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for n in nums:
            if n in hset:
                return True
            else:
                hset.add(n)
        return False