class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        edgeList = {v: [] for v in range(n)}
        for u, v in edges:
            if u == v:
                return False
            edgeList[u].append(v)
            edgeList[v].append(u)
        
        visited, path = set(), set()
        def dfs(v, source):
            if v in path:
                return False
            if v in visited:
                return True
            
            path.add(v)
            for u in edgeList[v]:
                if u == source:
                    continue
                if not dfs(u, v):
                    return False
            path.remove(v)
            visited.add(v)
            return True
        
        return dfs(0, 0) and len(visited) == n
