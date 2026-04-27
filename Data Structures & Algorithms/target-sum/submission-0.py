class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        visited = set()
        count = 0

        def dfs(i, currSum):
            nonlocal count
            if (i, currSum) in visited:
                return
            if i == len(nums):
                if currSum == target:
                    count += 1
                return
            
            dfs(i + 1, currSum + nums[i])
            dfs(i + 1, currSum - nums[i])
        
        dfs(0, 0)
        return count