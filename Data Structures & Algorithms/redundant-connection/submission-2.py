class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjList = {v: [] for v in range(1, len(edges) + 1)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited, cycle = set(), set()
        cycleStart = 0
        def dfs(v, s):
            nonlocal cycleStart
            if v in visited:
                cycleStart = v
                return True
            
            visited.add(v)
            for u in adjList[v]:
                if u == s:
                    continue
                if dfs(u, v):
                    if cycleStart != 0:
                        cycle.add(v)
                    if v == cycleStart:
                        cycleStart = 0
                    return True
            
            return False
        
        dfs(1, 0)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
            