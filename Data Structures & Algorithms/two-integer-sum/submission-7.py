class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, n in enumerate(nums):
            if n not in targets:
                targets[target - n] = i
            else:
                return [targets[n], i]
        
        return [-1, -1]