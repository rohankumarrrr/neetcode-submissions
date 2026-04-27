class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        subset = []
        def dfs(i, subsetSum):
            if totalSum - subsetSum == subsetSum:
                return True
            if i == len(nums):
                return False
            subset.append(nums[i])
            flag = dfs(i + 1, subsetSum + nums[i])
            subset.pop()
            return flag or dfs(i + 1, subsetSum)
        
        return dfs(0, 0)