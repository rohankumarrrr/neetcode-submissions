# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr1, curr2 = dummy, head

        for i in range(n):
            curr2 = curr2.next

        while curr2:
            curr1 = curr1.next
            curr2 = curr2.next

        curr1.next = curr1.next.next
        return dummy.next