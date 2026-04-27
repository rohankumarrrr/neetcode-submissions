"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}
        def dfs(curr):
            copy = Node(curr.val)
            visited[curr] = copy
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    copy.neighbors.append(visited[neighbor])
                else:
                    copy.neighbors.append(dfs(neighbor))
            return visited[curr]
        
        if not node:
            return None
        return dfs(node)
        


