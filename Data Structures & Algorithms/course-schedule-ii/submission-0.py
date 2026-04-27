class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        order = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order


