class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // len(matrix[0]), m % len(matrix[0])
            if target < matrix[row][col]:
                r = m - 1
            elif target > matrix[row][col]:
                l = m + 1
            else:
                return True

        return False