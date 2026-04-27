class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(r, c, board):
            rows = r - 1
            while rows >= 0:
                if board[rows][c] == 'Q':
                    return False
                rows -= 1
            rows, cols = r - 1, c - 1
            while rows >= 0 and cols >= 0:
                if board[rows][cols] == 'Q':
                    return False
                rows -= 1
                cols -= 1
            rows, cols = r - 1, c + 1
            while rows >= 0 and cols < n:
                if board[rows][cols] == 'Q':
                    return False
                rows -= 1
                cols += 1
            return True

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if isValid(r, c, board):
                    board[r][c] = 'Q'
                    dfs(r + 1)
                    board[r][c] = '.'
        
        dfs(0)
        return res
