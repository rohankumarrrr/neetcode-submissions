# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = defaultdict(list)
        q = deque()
        if not root:
            return []
        q.appendleft((root, 0))

        while q:
            currNode, currLevel = q.pop()
            levels[currLevel].append(currNode.val)
            if currNode.right:
                q.append((currNode.right, currLevel + 1))
            if currNode.left:
                q.append((currNode.left, currLevel + 1))
        
        return [v for k, v in levels.items()]
