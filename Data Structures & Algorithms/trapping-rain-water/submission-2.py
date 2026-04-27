class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                max_left = max(height[left], max_left)
                res += max_left - height[left]
            else:
                right -= 1
                max_right = max(height[right], max_right)
                res += max_right - height[right]
        
        return res

        