class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        targets = {}
        for i, num in enumerate(nums):
            if target - num in targets:
                return [targets[target - num], i]
            targets[num] = i
        
        return [-1, -1]