class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [(0, heights[0])]

        for i in range(1, len(heights)):
            currHeight = heights[i]
            start = i
            while stack and currHeight < stack[-1][1]:
                prevI, prevHeight = stack.pop()
                maxArea = max(maxArea, prevHeight * (i - prevI))
                start = prevI
            stack.append((start, currHeight))
        
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        
        return maxArea
            