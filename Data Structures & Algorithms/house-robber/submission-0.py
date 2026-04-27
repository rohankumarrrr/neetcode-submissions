class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        # memo[i] is the maximum amount of money we can rob considering nums[0...i]
        memo = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(nums[i], memo[i - 1])
            else:
                memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        
        return memo[-1]