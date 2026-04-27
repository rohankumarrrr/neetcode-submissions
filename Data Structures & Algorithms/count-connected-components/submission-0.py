class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {v: [] for v in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        res = 0
        visited = set()

        def dfs(v):
            for u in adjList[v]:
                if not u in visited:
                    visited.add(u)
                    dfs(u)
        
        res = 0
        for v in range(n):
            if not v in visited:
                visited.add(v)
                dfs(v)
                res += 1
        return res
