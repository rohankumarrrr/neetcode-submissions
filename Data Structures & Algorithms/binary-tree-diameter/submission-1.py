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
            hL, hR = 1 + height(root.left), 1 + height(root.right)
            diameter = max(diameter, hL + hR)
            return max(hL, hR)
        
        height(root)
        return diameter