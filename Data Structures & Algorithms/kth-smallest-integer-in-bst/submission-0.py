# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        dfs = [root]
        while dfs:
            curr = dfs[-1]
            heapq.heappush(heap, curr.val)
            dfs.pop()
            if curr.left:
                dfs.append(curr.left)
            if curr.right:
                dfs.append(curr.right)

        for i in range(k - 1):
            heapq.heappop(heap)
        
        return heap[0]
        
            
            
