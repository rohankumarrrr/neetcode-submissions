class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        parent = [v for v in range(n + 1)]
        rank = [1] * (n + 1)

        def findParent(v):
            if not v == parent[v]:
                parent[v] = findParent(parent[v])
            return parent[v]
        
        def union(u, v):
            p1, p2 = findParent(u), findParent(v)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []
        
