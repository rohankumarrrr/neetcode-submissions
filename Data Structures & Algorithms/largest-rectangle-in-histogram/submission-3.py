class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, currHeight in enumerate(heights):
            start = i
            while stack and currHeight < stack[-1][1]:
                prevI, prevHeight = stack[-1]
                maxArea = max(maxArea, prevHeight * (i - prevI))
                start = prevI
                stack.pop()
            stack.append((start, currHeight))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea