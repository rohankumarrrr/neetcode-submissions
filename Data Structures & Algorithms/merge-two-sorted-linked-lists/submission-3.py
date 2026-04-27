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

        pos = newHead

        if newHead == list1:
            list1 = list1.next
        else:
            list2 = list2.next
        
        while True:
            if not (list1 or list2):
                break
            if list1 and list2:
                if list1.val < list2.val:
                    pos.next, list1 = list1, list1.next
                else:
                    pos.next, list2 = list2, list2.next
            elif not list2:
                pos.next, list1 = list1, list1.next
            else:
                pos.next, list2 = list2, list2.next
            pos = pos.next
        
        return newHead
