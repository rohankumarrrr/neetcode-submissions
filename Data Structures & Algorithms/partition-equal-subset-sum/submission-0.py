class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        totalSum = sum(nums)
        def dfs(i, subset, subsetSum):
            if totalSum - subsetSum == subsetSum:
                return True
            if i == len(nums):
                return False
            subset.append(nums[i])
            flag = dfs(i + 1, subset.copy(), subsetSum + nums[i])
            subset.pop()
            return flag or dfs(i + 1, subset.copy(), subsetSum)
        
        return dfs(0, [], 0)