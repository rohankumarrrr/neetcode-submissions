# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        a, b = p, q
        if b.val < a.val:
            a, b = b, a
        
        res = root
        def dfs(root):
            nonlocal res
            if not root:
                return
            if a.val <= root.val <= b.val:
                res = root
                return
            if a.val < b.val < root.val:
                dfs(root.left)
            else:
                dfs(root.right)
        
        dfs(root)
        return res