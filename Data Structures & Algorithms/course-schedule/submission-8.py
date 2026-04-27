class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {c: [] for c in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a)
        
        visited = set()
        path = set()
        def dfs(v):
            if v in path:
                return False
            if v in visited:
                return True
            
            path.add(v)
            for u in adjList[v]:
                if not dfs(u):
                    return False
            path.remove(v)
            visited.add(v)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True