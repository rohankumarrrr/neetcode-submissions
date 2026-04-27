"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        d = {}
        d[None] = None

        curr = head
        while curr:
            d[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        curr = head
        while curr:
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next
        
        return d[head]