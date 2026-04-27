class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            middle = left + (right - left) // 2
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            res = min(res, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return res