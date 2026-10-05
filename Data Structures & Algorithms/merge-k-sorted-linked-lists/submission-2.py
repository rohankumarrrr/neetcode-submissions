# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):

            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if not l1:
                curr.next = l2
            if not l2:
                curr.next = l1
            
            return dummy.next
        
        k = len(lists)
        if k > 2:
            return merge(self.mergeKLists(lists[: k // 2 + 1]), self.mergeKLists(lists[k // 2 + 1:]))
        if k == 2:
            return merge(lists[0], lists[1])
        if k == 1:
            return merge(lists[0], None)
        if k == 0:
            return None
