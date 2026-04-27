class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []

        def recursion(idx, current, total):
            if total == target:
                solution.append(current.copy())
                return
            if idx >= len(nums) or total > target:
                return
            
            current.append(nums[idx])
            recursion(idx, current, total + nums[idx])

            current.pop()
            recursion(idx + 1, current, total)
        
        recursion(0, [], 0)
        return solution