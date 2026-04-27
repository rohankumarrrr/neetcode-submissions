class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return max(nums)

        res = 0

        # choose to skip the last house
        secondToLast, last = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            secondToLast, last = last, max(last, secondToLast + nums[i])
        
        res = last

        # choose to skip the first house
        secondToLast, last = nums[1], max(nums[1], nums[2])

        for i in range(3, len(nums)):
            secondToLast, last = last, max(last, secondToLast + nums[i])
        
        return max(res, last)
        