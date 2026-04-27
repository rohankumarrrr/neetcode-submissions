class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        indegree = {v: 0 for v in range(1, n+1)}
        adjList = {v: [] for v in range(1, n+1)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()

        for v in range(1, n+1):
            if indegree[v] == 1:
                q.appendleft(v)
        
        while q:
            for _ in range(len(q)):
                v = q.pop()
                indegree[v] -= 1
                for u in adjList[v]:
                    indegree[u] -= 1
                    if indegree[u] == 1:
                        q.appendleft(u)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v] > 0:
                return [u, v]
        
        return []
