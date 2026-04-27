class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            middle = top + (bottom - top) // 2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break
        
        if top > bottom:
            return False
        
        row = top + (bottom - top) // 2
        left, right = 0, len(matrix[0]) - 1
        
        while left <= right:
            middle = left + (right - left) // 2
            if target == matrix[row][middle]:
                return True
            elif target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
        
        return False
