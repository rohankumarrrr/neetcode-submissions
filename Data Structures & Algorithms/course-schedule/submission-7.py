class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqs = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            prereqs[c].append(p)
        
        path = set()

        def dfs(c):
            if c in path:
                return False
            if prereqs[c] == []:
                return True
            path.add(c)
            for p in prereqs[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            prereqs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
                