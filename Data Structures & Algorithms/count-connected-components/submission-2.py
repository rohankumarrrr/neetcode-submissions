class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {v: [] for v in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(v):
            visited.add(v)
            for u in adjList[v]:
                if not u in visited:
                    dfs(u)
        
        res = 0
        for v in range(n):
            if v in visited:
                continue
            dfs(v)
            res += 1

        return res