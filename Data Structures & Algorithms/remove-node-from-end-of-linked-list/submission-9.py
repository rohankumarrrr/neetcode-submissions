# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = dummy = ListNode(0, head)
        slow, fast = head, head

        for _ in range(n):
            fast = fast.next

        while fast:
            prev, slow, fast = slow, slow.next, fast.next
        
        prev.next = slow.next
        return dummy.next

