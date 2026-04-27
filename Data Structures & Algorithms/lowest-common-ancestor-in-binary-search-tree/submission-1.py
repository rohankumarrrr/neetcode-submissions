# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        a, b = p, q
        if q.val < p.val:
            a, b = b, a

        def dfs(root):
            if a.val < root.val and root.val < b.val:
                return root
            if a.val < root.val and b.val < root.val:
                return dfs(root.left)
            if a.val > root.val and b.val > root.val:
                return dfs(root.right)
            if a.val == root.val or b.val == root.val:
                return root
        
        return dfs(root)