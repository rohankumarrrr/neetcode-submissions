class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + n > 0:
                    right -= 1
                elif nums[left] + nums[right] + n < 0:
                    left += 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return res
                    