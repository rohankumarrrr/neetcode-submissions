class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for x in nums:
            if x - 1 in numset:
                continue
            length = 1
            while x + length in numset:
                length += 1
            longest = max(longest, length)
        
        return longest