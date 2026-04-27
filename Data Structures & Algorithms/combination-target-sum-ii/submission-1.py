class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        combination = []
        candidates.sort()

        # [1, 2, 2, 4, 5, 6, 9]

        def dfs(total, i):
            if total == target:
                res.append(combination.copy())
                return
            if total > target or i == len(candidates):
                return
            combination.append(candidates[i])
            dfs(total + candidates[i], i + 1)
            combination.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(total, i + 1)
        
        dfs(0, 0)
        return res