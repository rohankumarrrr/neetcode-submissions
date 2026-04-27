class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums)):
            x = nums[i]
            target = -nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            else:
                left, right = i + 1, len(nums) - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        res.append([x, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return res
            
                
                

            
            
            
