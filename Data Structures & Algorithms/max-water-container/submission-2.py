class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left, right = 0, len(heights) - 1
        while left < right:
            x, y = right - left, min(heights[left], heights[right])
            A = x * y

            res = max(res, A)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res

