class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        combination = []

        def dfs(total, i):
            if total == target:
                res.append(combination.copy())
                return
            if total > target or i >= len(nums):
                return
            
            combination.append(nums[i])
            dfs(total + nums[i], i)
            combination.pop()
            dfs(total, i + 1)
        
        dfs(0, 0)
        return res