class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n - 1:
            return False
        
        adjList = {v: [] for v in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        path = set()
        def dfs(v, s):
            if v in path:
                return
            
            path.add(v)

            for u in adjList[v]:
                if u == s:
                    continue
                dfs(u, v)
        
        dfs(0, -1)
        return len(path) == n

