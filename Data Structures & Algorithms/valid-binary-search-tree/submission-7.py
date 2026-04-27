# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(lower, root, upper):
            if not root:
                return True
            if not lower < root.val < upper:
                return False
            return valid(lower, root.left, root.val) and valid(root.val, root.right, upper)
        
        return valid(float("-inf"), root, float("inf"))