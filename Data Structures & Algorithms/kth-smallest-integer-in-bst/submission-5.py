# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        preorder = []

        def dfs(root):
            nonlocal preorder
            if not root:
                return
            dfs(root.left)
            preorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return preorder[k - 1]