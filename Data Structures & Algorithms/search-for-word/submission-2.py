class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if (not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in visited or not word[i] == board[r][c]):
                return False
            if i == len(word) - 1:
                return True
            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False