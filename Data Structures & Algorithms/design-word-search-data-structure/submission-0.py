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
        def find(node, word):
            if not word:
                return node.endOfWord
            if word[0] == '.':
                for child in node.children:
                    if find(node.children[child], word[1:]):
                        return True
                return False
            if word[0] not in node.children:
                return False
            return find(node.children[word[0]], word[1:])

        return find(self.root, word)


