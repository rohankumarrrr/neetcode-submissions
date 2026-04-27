from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {c: set() for word in words for c in word}
        incomingEdges = {c: 0 for c in adjList.keys()}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adjList[w1[j]]:
                        adjList[w1[j]].add(w2[j])
                        incomingEdges[w2[j]] += 1
                    break
        
        q = deque()

        for c, cnt in incomingEdges.items():
            if cnt == 0:
                q.appendleft(c)
        
        ordering = []

        while q:
            c = q.pop()

            ordering.append(c)

            for nei in adjList[c]:
                incomingEdges[nei] -= 1
                if incomingEdges[nei] == 0:
                    q.appendleft(nei)

        if not len(ordering) == len(adjList):
            return ""

        return ''.join(ordering)
            
