class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (right - left) * min(heights[left], heights[right])
        left, right = 0, len(heights) - 1
        # Input : [1, 7, 2, 5, 4, 7, 3, 6]
        A = 0
        while left < right:
            A = max(A, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return A
