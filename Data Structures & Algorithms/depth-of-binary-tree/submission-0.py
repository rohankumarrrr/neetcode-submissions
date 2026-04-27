# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if (not root.left and not root.right):
            return 1
        if (root.left and not root.right):
            return 1 + self.maxDepth(root.left)
        if (not root.left and root.right):
            return 1 + self.maxDepth(root.right)
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if leftDepth > rightDepth:
            return 1 + leftDepth
        return 1 + rightDepth