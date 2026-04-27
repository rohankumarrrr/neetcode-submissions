class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Pick ith element, loop from i to end to find equal
        for i in range(0, len(nums) - 1):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                if (nums[j] == current):
                    return True
        return False     