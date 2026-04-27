class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            curr, target = nums[i], -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    res.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
        return res
