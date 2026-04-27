class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(nums[i], memo[i - 1])
            else:
                memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        
        return memo[-1]