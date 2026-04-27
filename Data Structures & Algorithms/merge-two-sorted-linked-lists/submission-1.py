# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_list = dummy
        while (list1 is not None or list2 is not None):
            if (list1 is None or list2 is not None and list2.val < list1.val):
                new_list.next = list2
                list2 = list2.next
            elif (list2 is None or list1 is not None and list1.val <= list2.val):
                new_list.next = list1
                list1 = list1.next
            new_list = new_list.next
        return dummy.next
            