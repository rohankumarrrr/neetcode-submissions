class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(point):
            x, y = point
            return (x ** 2 + y ** 2) ** 0.5
        
        nums = [[getDistance(point), point] for point in points]

        def quickSelect(l, r):
            pivot, part = nums[r], l
            for i in range(l, r):
                if nums[i][0] <= pivot[0]:
                    nums[i], nums[part] = nums[part], nums[i]
                    part += 1
            nums[part], nums[r] = nums[r], nums[part]
            if part > k - 1:
                return quickSelect(l, part - 1)
            if part < k - 1:
                return quickSelect(part + 1, r)
            return part
        
        quickSelect(0, len(nums) - 1)
        return [point for _, point in nums[:k]]