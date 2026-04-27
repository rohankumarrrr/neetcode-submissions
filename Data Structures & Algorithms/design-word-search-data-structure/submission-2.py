# Trie
# starts with a root node
# root node contains a collection of children, where each child represents the first character of a word in our dictionary
# each children of the root contains a collection of children, where each child represents the second character of a word in our dictionary that has the parent as its first character
# so on and so forth

# input: "da.s"
# insert "days"
# search "da"
# root0(Null) -> level1("d") -> level2("a") -> level3("y") -> level4("s")
#                                           -> level3("d")

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # char c -> TrieNode(c)
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:

        def dfs(curr, i):
            
            if i == len(word):
                return curr.isEndOfWord

            if word[i] == '.':
                wordExists = False
                for c in curr.children:
                    wordExists = wordExists or dfs(curr.children[c], i + 1)
                return wordExists

            if word[i] not in curr.children:
                return False
            
            return dfs(curr.children[word[i]], i + 1)
        
        return dfs(self.root, 0)
                

        
