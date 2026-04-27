class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = (0, nums[0])
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r] and nums[l] < pivot[1]:
                pivot = (l, nums[l])
                break
            m = l + (r - l) // 2
            if nums[m] < pivot[1]:
                pivot = (m, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        l, r = 0, pivot[0] - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        l, r = pivot[0], len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1