class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        permutation = []

        def dfs(chosen):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for j in range(len(nums)):
                if not chosen[j]:
                    chosen[j] = True
                    permutation.append(nums[j])
                    dfs(chosen.copy())
                    chosen[j] = False
                    permutation.pop()
        
        dfs([False] * len(nums))
        return res
