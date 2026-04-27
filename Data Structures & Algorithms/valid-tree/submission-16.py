class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # One connected component
        # Acylic

        adjList = {v: [] for v in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        path = set()

        def dfs(v, s):
            if v in path:
                return False
            
            path.add(v)
            for u in adjList[v]:
                if u == s:
                    continue
                if not dfs(u, v):
                    return False

            return True
        
        return dfs(0, -1) and len(path) == n