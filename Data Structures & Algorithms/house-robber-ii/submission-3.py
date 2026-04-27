class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(nums):
            first, second = nums[0], max(nums[:2])
            for i in range(2, len(nums)):
                tmp = second
                second = max(second, nums[i] + first)
                first = tmp
            
            return second
        
        return max(dp(nums[1:]), dp(nums[:-1])) if len(nums) > 1 else nums[0]