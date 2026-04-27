"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        ogToCopy = {}

        def dfs(v):
            if v in ogToCopy:
                return ogToCopy[v]
            
            copy = Node(v.val)
            ogToCopy[v] = copy

            for nei in v.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return ogToCopy[v]
        
        return dfs(node) if node else None
