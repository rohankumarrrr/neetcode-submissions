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

        while root:
            if a.val < b.val < root.val:
                root = root.left
            elif root.val < a.val < b.val:
                root = root.right
            else:
                return root
        
        return dfs(root)