class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top, row_bottom = 0, len(matrix) - 1
        row_target = -1
        while row_top <= row_bottom:
            middle = row_top + (row_bottom - row_top) // 2
            if matrix[middle][-1] < target:
                row_top = middle + 1
            if matrix[middle][0] > target:
                row_bottom = middle - 1
            else:
                break
        
        if row_top > row_bottom:
            return False
        row_target = row_top + (row_bottom - row_top) // 2
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if matrix[row_target][middle] < target:
                left = middle + 1
            elif matrix[row_target][middle] > target:
                right = middle - 1
            else:
                return True
        return False 