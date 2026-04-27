class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        order = []
        taken, path = set(), set()
        def dfs(course):
            if course in path:
                return False
            if course in taken:
                return True
            
            path.add(course)
            for p in prereqs[course]:
                if not dfs(p):
                    return False
            
            path.remove(course)
            order.append(course)
            taken.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order