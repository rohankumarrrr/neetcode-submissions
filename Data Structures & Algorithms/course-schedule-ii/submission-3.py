class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        
        order = []
        visited, path = set(), set()
        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True

            path.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            visited.add(c)
            order.append(c)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return order