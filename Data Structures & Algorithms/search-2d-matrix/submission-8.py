class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COL = -1, -1
        
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            r = top + (bottom - top) // 2
            if target < matrix[r][0]:
                bottom = r - 1
            elif target > matrix[r][-1]:
                top = r + 1
            else:
                ROW = r
                break
        
        if ROW == -1:
            return False
        
        left, right = 0, len(matrix[ROW]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[ROW][mid]:
                right = mid - 1
            elif target > matrix[ROW][mid]:
                left = mid + 1
            else:
                COL = mid
                return True
        
        return False

