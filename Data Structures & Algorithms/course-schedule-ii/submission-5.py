class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {c: [] for c in range(numCourses)}
        for a, b in prerequisites:
            adjList[b].append(a)
        
        order = []
        visited = set()
        path = set()

        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            
            path.add(c)
            for n in adjList[c]:
                if not dfs(n):
                    return False
            path.remove(c)
            visited.add(c)
            order.append(c)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order[::-1]