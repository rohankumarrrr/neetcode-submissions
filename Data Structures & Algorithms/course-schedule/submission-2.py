class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereqs = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        def dfs(course, path):
            if course in path:
                return False
            if not prereqs[course]:
                return True
            
            path.add(course)
            for p in prereqs[course]:
                if not dfs(p, path):
                    return False
            
            prereqs[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        
        return True