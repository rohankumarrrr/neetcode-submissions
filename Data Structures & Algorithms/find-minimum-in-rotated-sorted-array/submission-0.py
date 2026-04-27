class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        curr_min = float("inf")

        while left < right:
            middle = left + (right - left) // 2
            curr_min = min(curr_min, nums[middle])

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        
        return min(curr_min, nums[left])