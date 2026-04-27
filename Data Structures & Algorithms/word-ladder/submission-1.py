from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet or beginWord == endWord:
            return 0
        
        def isValidTransformation(start, end):
            diff = 0
            for i in range(len(start)):
                if not start[i] == end[i]:
                    diff += 1

            return diff == 1


        q = deque()
        visited = set()

        q.appendleft(beginWord)
        visited.add(beginWord)

        dist = 1
        while q:
            for _ in range(len(q)):
                curr = q.pop()

                for word in wordSet:
                    if word in visited or not isValidTransformation(curr, word):
                        continue
                    
                    if word == endWord:
                        return dist + 1

                    q.appendleft(word)
                    visited.add(word)
            dist += 1
        
        return 0