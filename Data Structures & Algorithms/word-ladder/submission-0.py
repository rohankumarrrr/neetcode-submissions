from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + "*" + word[c+1:]
                adjList[pattern].append(word)
        
        visited, q = set(), deque()
        visited.add(beginWord)
        q.appendleft(beginWord)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.pop()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c + 1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            q.appendleft(neighbor)
                            visited.add(neighbor)
            res += 1
        
        return 0