"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        copyMap = {}

        def dfs(v):
            if v in copyMap:
                return copyMap[v]
            copy = Node(v.val)
            copyMap[v] = copy
            for u in v.neighbors:
                copy.neighbors.append(dfs(u))
            return copy
        
        return dfs(node) if node else None