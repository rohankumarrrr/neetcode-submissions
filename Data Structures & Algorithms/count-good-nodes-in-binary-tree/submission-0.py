# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def good(root, maxVal):
            if not root:
                return 0
            res = 0
            if root.val >= maxVal:
                res += 1
            res += good(root.left, max(root.val, maxVal))
            res += good(root.right, max(root.val, maxVal))
            return res

        return good(root, root.val)