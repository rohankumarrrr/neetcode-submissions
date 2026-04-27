# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root, leftVal, rightVal):
            if not root:
                return True
            if not leftVal < root.val < rightVal:
                return False
            return bst(root.left, leftVal, root.val) and bst(root.right, root.val, rightVal)
        
        return bst(root, float("-inf"), float("inf"))