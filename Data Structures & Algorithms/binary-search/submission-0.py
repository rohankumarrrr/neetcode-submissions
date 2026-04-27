class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        middle = len(nums) // 2

        while (left <= right):
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
                middle = left + (right - left) // 2
            else:
                left = middle + 1
                middle = left + (right - left) // 2
        
        return -1