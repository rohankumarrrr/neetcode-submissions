class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        solution = []
        subset = []
        def recursion(i):
            if i >= len(nums):
                solution.append(subset.copy())
                return
            
            subset.append(nums[i])
            recursion(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            recursion(i + 1)
        
        recursion(0)
        return solution