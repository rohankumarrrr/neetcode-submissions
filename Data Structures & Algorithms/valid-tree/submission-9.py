class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n - 1:
            return False

        adjList = {v: [] for v in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(v, s):
            if v in visited:
                return False
            
            visited.add(v)
            for u in adjList[v]:
                if u == s:
                    continue
                if not dfs(u, v):
                    return False
            
            return True
        
        return dfs(0, 0) and len(visited) == n
            