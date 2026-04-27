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
            hL, hR = height(root.left), height(root.right)
            if abs(hL - hR) > 1:
                return -1
            if hL == -1 or hR == -1:
                return -1
            return max(hL, hR) + 1
        
        return not height(root) == -1