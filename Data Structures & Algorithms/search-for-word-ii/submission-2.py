class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(row, col, node, word):
            
            if (not 0 <= row < ROWS
                or not 0 <= col < COLS
                or (row, col) in visited
                or not board[row][col] in node.children):
                return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                res.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visited.remove((row, col))
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        
        return list(res)