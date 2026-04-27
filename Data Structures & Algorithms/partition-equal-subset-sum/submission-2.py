class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        if (totalSum % 2 == 1):
            return False
        
        target = totalSum / 2

        visited = set()

        def dfs(i, currSum):
            if currSum > target or (i, currSum) in visited:
                return False
            if i == len(nums):
                return currSum == target

            visited.add((i, currSum))
            return dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum)
        
        return dfs(0, 0)
