class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 1. Single connected component
        # 2. No cycles

        if len(edges) > n - 1:
            return False

        adjList = {i: [] for i in range(n)}
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