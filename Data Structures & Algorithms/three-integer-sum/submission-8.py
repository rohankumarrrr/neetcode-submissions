class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                return res
            while i < len(nums) and i > 0 and nums[i] == nums[i - 1]:
                i += 1
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            i += 1
        
        return res
                    