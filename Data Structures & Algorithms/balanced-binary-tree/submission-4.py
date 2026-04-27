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
            
            h1, h2 = height(root.left), height(root.right)
            if h1 == -1 or h2 == -1 or abs(h1 - h2) > 1:
                return -1

            return max(h1, h2) + 1
        
        return not height(root) == -1