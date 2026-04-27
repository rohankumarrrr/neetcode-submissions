# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            
            h1 = height(root.left)
            if h1 == -1:
                return -1

            h2 = height(root.right)
            if h2 == -1:
                return -1

            if abs(h1 - h2) > 1:
                return -1

            return max(h1, h2) + 1
        
        return not height(root) == -1