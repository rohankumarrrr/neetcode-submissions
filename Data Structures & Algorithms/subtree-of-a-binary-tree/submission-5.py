# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if not p.val == q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)
        
        if not root and subRoot:
            return False
        if not root:
            return True

        stack = [root]
        while stack:
            curr = stack.pop()
            if same(curr, subRoot):
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return False
