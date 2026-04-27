# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0, head)
        prev, curr = dummy, head
        for i in range(length - n):
            prev, curr = curr, curr.next
        
        prev.next = curr.next
        return dummy.next