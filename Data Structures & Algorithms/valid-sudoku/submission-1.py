from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if not curr == ".":
                    g = (r // 3, c // 3)
                    if curr in rows[r] or curr in cols[c] or curr in grids[g]:
                        return False
                    rows[r].add(curr)
                    cols[c].add(curr)
                    grids[g].add(curr)
        
        return True