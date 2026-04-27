class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        maxRun = 0


        for num in numSet:
            if num - 1 not in numSet:
                i = 0
                while num + i in numSet:
                    i += 1
                maxRun = max(maxRun, i)
        
        return maxRun