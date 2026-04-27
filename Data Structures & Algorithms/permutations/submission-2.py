class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        permutation = []

        def dfs(chosen):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            for i in range(len(nums)):
                if not chosen[i]:
                    chosen[i] = True
                    permutation.append(nums[i])
                    dfs(chosen.copy())
                    chosen[i] = False
                    permutation.pop()
        
        dfs([False] * len(nums))
        return res