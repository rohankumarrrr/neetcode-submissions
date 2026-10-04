class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A Graph G is also a tree T iff
        # G has exactly one root node
        # G is acylic
        
        # G has exactly (n - 1) edges
        if len(edges) != n - 1:
            return False
        
        # G has exactly one connected component
        adjList = {i: set() for i in range(n)}
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)
        
        seen = set()
        def dfs(u):
            seen.add(u)
            for v in adjList[u]:
                if v not in seen:
                    dfs(v)
        
        dfs(0)
        if len(seen) != n:
            return False
        
        return True

