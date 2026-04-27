class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(l, r):
            pivot, partition = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    partition += 1
            nums[r], nums[partition] = nums[partition], nums[r]
            if partition > len(nums) - k:
                quickSelect(l, partition - 1)
            if partition < len(nums) - k:
                quickSelect(partition + 1, r)
            return
        
        quickSelect(0, len(nums) - 1)
        return nums[len(nums) - k]