class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {v: [] for v in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(v, s):
            if v in visited:
                return 0
            visited.add(v)
            for u in adjList[v]:
                if u == s:
                    continue
                dfs(u, v)
            return 1
        
        res = 0
        for v in range(n):
            res += dfs(v, -1)
        
        return res