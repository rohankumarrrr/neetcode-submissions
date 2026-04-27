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
        
        ogToCopy = defaultdict(lambda: Node(0))
        ogToCopy[None] = None

        curr = head
        while curr:
            ogToCopy[curr].val = curr.val
            ogToCopy[curr].next = ogToCopy[curr.next]
            ogToCopy[curr].random = ogToCopy[curr.random]
            curr = curr.next
        
        return ogToCopy[head]