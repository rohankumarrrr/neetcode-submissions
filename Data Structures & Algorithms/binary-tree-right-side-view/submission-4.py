# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        levels = defaultdict(list)
        q = deque()
        q.appendleft((root, 0))

        while q:
            currNode, currLevel = q.pop()
            levels[currLevel].append(currNode.val)

            if currNode.left:
                q.appendleft((currNode.left, currLevel + 1))
            if currNode.right:
                q.appendleft((currNode.right, currLevel + 1))
        
        return [v[-1] for k, v in levels.items()]
