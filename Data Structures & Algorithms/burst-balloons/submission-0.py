class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        memo = {}

        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            
            memo[(left, right)] = 0
            for i in range(left, right + 1):
                profit = nums[left - 1] * nums[i] * nums[right + 1] + dfs(i + 1, right) + dfs(left, i - 1)
                memo[(left, right)] = max(memo[(left, right)], profit)
            return memo[(left, right)]
        
        return dfs(1, len(nums) - 2)

