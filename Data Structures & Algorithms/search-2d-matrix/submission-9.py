class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCandidate = -1
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                rowCandidate = m
                break
        
        if rowCandidate < 0:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[rowCandidate][m]:
                r = m - 1
            elif target > matrix[rowCandidate][m]:
                l = m + 1
            else:
                return True
        
        return False