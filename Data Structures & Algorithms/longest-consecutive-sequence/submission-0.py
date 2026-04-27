class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_count = 0
        for x in nums:
            if x - 1 not in s:
                length = 0
                while (x + length in s):
                    length += 1
                max_count = max(length, max_count)
        return max_count