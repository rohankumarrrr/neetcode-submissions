class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        goal = {}

        for i, x in enumerate(nums):
            if target - x in goal:
                return [goal[target - x], i]
            goal[x] = i
        
        return []