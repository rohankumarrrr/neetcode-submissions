class Solution:
    def rob(self, nums: List[int]) -> int:
        
        secondToLast, last = -1, -1

        for i in range(len(nums)):
            if i == 0:
                last = nums[i]
            elif i == 1:
                secondToLast, last = last, max(nums[i], last)
            else:
                secondToLast, last = last, max(nums[i] + secondToLast, last)
        
        return last