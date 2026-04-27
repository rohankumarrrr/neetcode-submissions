class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeftHeight, maxRightHeight = -1, -1
        trap = 0
        while left < right:
            maxLeftHeight = max(height[left], maxLeftHeight)
            maxRightHeight = max(height[right], maxRightHeight)
            if maxLeftHeight < maxRightHeight:
                trap += max(maxLeftHeight - height[left], 0)
                left += 1
            else:
                trap += max(maxRightHeight - height[right], 0)
                right -= 1

        return trap