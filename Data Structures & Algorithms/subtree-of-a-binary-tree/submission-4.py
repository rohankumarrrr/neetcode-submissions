# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or not root1.val == root2.val:
                return False
            return same(root1.left, root2.left) and same(root1.right, root2.right)
        
        if not root and not subRoot:
            return True
        
        if not root:
            return False

        stack = [root]
        while stack:
            node = stack.pop()
            if same(node, subRoot):
                return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return False



