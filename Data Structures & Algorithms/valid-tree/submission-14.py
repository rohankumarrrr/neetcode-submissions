class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 1. A single connected component
        # 2. Exactly n - 1 edges for n nodes
        # 3. Acylic

        # 2. n - 1 edges -> len(edges) == n - 1
        if len(edges) != n - 1:
            return False
        
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        # 3. Acylic -> Run a whatever-first search to detect cycles
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
        # 1. A single connected component -> when we
        # run a whatever-first search from any starting
        # node on the graph, we should reach all nodes
        return len(path) == n
        
