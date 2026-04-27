class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n - 1:
            return False

        edgeList = {v: [] for v in range(n)}
        for u, v in edges:
            edgeList[u].append(v)
            edgeList[v].append(u)
        
        visited, path = set(), set()
        def dfs(v, source):
            if v in path:
                return False
            
            path.add(v)
            for u in edgeList[v]:
                if u == source:
                    continue
                if not dfs(u, v):
                    return False
            return True
        
        return dfs(0, 0) and len(path) == n
