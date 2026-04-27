class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
    def addWord(self, word):
        curr = self
        for c in word:
            curr.next = ListNode(c)
            curr = curr.next

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, path):

            if (not 0 <= r < ROWS or
                not 0 <= c < COLS or
                not node.next.val == board[r][c] or
                (r, c) in visited):

                return False
            
            visited.add((r, c))
            path += board[r][c]
            node = node.next
            if path == word:
                return True
            
            res = (dfs(r + 1, c, node, path) or
            dfs(r - 1, c, node, path) or
            dfs(r, c + 1, node, path) or
            dfs(r, c - 1, node, path))

            visited.remove((r, c))
            return res

        head = ListNode('')
        head.addWord(word)

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, head, ""):
                    return True

        return False



