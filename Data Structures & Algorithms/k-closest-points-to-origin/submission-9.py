class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        nums = []
        for point in points:
            nums.append([getDistance(point), point])
        
        def quickSelect(l, r):
            pivot, partition = nums[r], l
            for i in range(l, r):
                if nums[i][0] <= pivot[0]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    partition += 1
            nums[r], nums[partition] = nums[partition], nums[r]
            if partition > k - 1:
                quickSelect(l, partition - 1)
            if partition < k - 1:
                quickSelect(partition + 1, r)
            return
        
        quickSelect(0, len(points) - 1)
        return [point for _, point in nums[:k]]