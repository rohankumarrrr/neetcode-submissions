class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # A collection of vertices C is connected if and only if
        # for each pair of vertices (u, v) in C, there exists
        # a path from u to v

        # [[0,1], [1,2], [2,3], [4,5]]

        # 0: [1]
        # 1: [0, 2]
        # 2: [1, 3]
        # 3: [2]

        # 4: [5]
        # 5: [4]

        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(v, s):
            if v in visited:
                return 0
            visited.add(v)
            for u in adjList[v]:
                if u == s:
                    continue
                dfs(u, v)
            return 1
        
        numConnectedComponents = 0
        for v in range(n):
            numConnectedComponents += dfs(v, -1)
        
        return numConnectedComponents

