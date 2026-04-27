class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ROWS, COLS = n, n
        res = []
        board = [['.' for _ in range(n)] for _ in range(n) ]

        def isValid(r, c, board):
            row = r - 1
            while row >= 0:
                if board[row][c] == 'Q':
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < COLS:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            return True 

        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(COLS):
                if isValid(r, c, board):
                    board[r][c] = "Q"
                    dfs(r + 1)
                    board[r][c] = "."
        
        dfs(0)
        return res
