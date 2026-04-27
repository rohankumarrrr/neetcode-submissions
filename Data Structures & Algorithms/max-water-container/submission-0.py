class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = -1
        while (left < right):
            left_bar = heights[left]
            right_bar = heights[right]
            area = max(area, min(left_bar, right_bar) * (right - left))
            if (left_bar < right_bar):
                left += 1
            else:
                right -= 1
        return area