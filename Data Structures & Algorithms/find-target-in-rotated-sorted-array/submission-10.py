class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def binarySearch(left, right):
            
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] < target:
                    left = m + 1
                elif nums[m] > target:
                    right = m - 1
                else:
                    return m
            
            return -1
        
        return max(binarySearch(0, pivot - 1), binarySearch(pivot, len(nums) - 1))