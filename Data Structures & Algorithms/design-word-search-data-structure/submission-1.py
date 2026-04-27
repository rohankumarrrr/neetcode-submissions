class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(curr, word):
            if not word:
                return curr.endOfWord
            if word[0] == ".":
                for c in curr.children:
                    if dfs(curr.children[c], word[1:]):
                        return True
                return False
            if word[0] not in curr.children:
                return False
            return dfs(curr.children[word[0]], word[1:])
        
        return dfs(self.root, word)
