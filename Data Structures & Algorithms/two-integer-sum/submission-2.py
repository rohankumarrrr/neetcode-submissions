class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            x = nums[i]
            y = target - x
            if (y in nums[i + 1:None]):
                j = nums[i + 1:None].index(y) + i + 1
                return [i, j]
        return []