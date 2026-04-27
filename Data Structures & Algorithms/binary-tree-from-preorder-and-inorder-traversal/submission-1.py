# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            i = 0
            while i < len(inorder) and inorder[i] != preorder[0]:
                i += 1
            
            root.left = build(preorder[1:i + 1], inorder[:i])
            root.right = build(preorder[i + 1:], inorder[i + 1:])

            return root
        
        return build(preorder, inorder)