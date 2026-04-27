class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p > len(nums) - k:
                return quickSelect(l, p - 1)
            if p < len(nums) - k:
                return quickSelect(p + 1, r)
            return nums[p]
        
        return quickSelect(0, len(nums) - 1)