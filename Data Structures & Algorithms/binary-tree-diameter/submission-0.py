# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def height(root):
            nonlocal diameter
            
            if not root:
                return -1

            h1, h2 = 1 + height(root.left), 1 + height(root.right)
            diameter = max(diameter, h1 + h2)

            return max(h1, h2)
        
        height(root)
        return diameter