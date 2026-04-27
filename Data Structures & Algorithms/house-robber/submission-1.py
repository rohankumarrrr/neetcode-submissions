class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        # memo[i] is the maximum amount of money we can rob considering nums[0...i]
        # memo1 = [0] * len(nums)
        # memo2 = (0, 0), where memo2[0] represents memo1[i - 2], and memo2[1] represents memo1[i - 1]
        memo = [0, 0]
        for i in range(len(nums)):
            if i == 0:
                memo[1] = nums[i]
            elif i == 1:
                memo = (memo[1], max(nums[i], memo[1]))
            else:
                memo = (memo[1], max(nums[i] + memo[0], memo[1]))
        
        return memo[-1]