class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i: set() for i in range(n)}
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)
        
        numConnectedComponents = 0
        seen = set()
        def dfs(u):
            seen.add(u)
            for v in adjList[u]:
                if v not in seen:
                    dfs(v)
        
        for u in range(n):
            if u not in seen:
                numConnectedComponents += 1
                dfs(u)
        
        return numConnectedComponents