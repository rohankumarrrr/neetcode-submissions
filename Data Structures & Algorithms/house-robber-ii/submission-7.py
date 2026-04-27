class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def dp(nums):
            if len(nums) == 1:
                return nums[0]

            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                first, second = second, max(second, first + nums[i])
            return second
        
        return max(dp(nums[1:]), dp(nums[:-1])) if len(nums) > 1 else nums[0]