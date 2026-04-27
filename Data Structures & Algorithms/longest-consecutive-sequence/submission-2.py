class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in s:
            if x - 1 not in s:
                length = 1
                while x + length in s:
                    length += 1
                res = max(res, length)
        return res