# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (list1 and list2):
            return list1 if not list2 else list2

        newHead = list1 if list1.val < list2.val else list2

        pos, curr1, curr2 = newHead, list1, list2

        if newHead == list1:
            curr1 = curr1.next
        else:
            curr2 = curr2.next
        
        while True:
            if not (curr1 or curr2):
                break
            if curr1 and curr2:
                if curr1.val < curr2.val:
                    pos.next, curr1 = curr1, curr1.next
                else:
                    pos.next, curr2 = curr2, curr2.next
            elif not curr2:
                pos.next, curr1 = curr1, curr1.next
            else:
                pos.next, curr2 = curr2, curr2.next
            pos = pos.next
        
        return newHead
