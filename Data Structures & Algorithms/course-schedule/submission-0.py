from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            d[course].append(prereq)
        
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if d[course] == []:
                return True
            
            visiting.add(course)
            for prereq in d[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            # d[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True