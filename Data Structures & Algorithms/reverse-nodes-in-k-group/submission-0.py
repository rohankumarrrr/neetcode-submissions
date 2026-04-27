# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head: Optional[ListNode]):
            prev = None
            curr = tail = head
            i = 0
            while i < k:
                currNext = curr.next
                curr.next = prev
                prev = curr
                curr = currNext
                i += 1
            
            return [prev, tail]


        dummy = ListNode(0)
        dummy.next = head
        prevTail = dummy
        curr = head

        while True:
            count = 0
            node = curr
            while node and count < k:
                node = node.next
                count += 1
            if count < k:
                prevTail.next = curr
                break

            groupHead = curr
            for _ in range(k):
                curr = curr.next
            newHead, newTail = reverse(groupHead)
            prevTail.next = newHead
            newTail.next = curr
            prevTail = newTail

        return dummy.next