class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        nums = [(distance(point), point) for point in points]

        def quickSelect(l, r):
            pivot, partition = nums[r][0], l
            for i in range(l, r):
                if nums[i][0] <= pivot:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    partition += 1
            nums[r], nums[partition] = nums[partition], nums[r]
            if partition > k - 1:
                quickSelect(l, partition - 1)
            if partition < k - 1:
                quickSelect(partition + 1, r)
            return
        
        quickSelect(0, len(nums) - 1)
        return [point for d, point in nums[:k]]