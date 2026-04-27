# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) < 2:
            return lists[0] if lists else None

        def merge(lists1, lists2):
            m, n = len(lists1), len(lists2)
            if m + n < 2:
                return lists1 if lists1 else lists2
            elif m + n > 2:
                return (merge(merge(lists1[:m // 2], lists1[m // 2:]), 
                    merge(lists2[:n // 2], lists2[n // 2:])))
            else:
                l1, l2 = lists1[0], lists2[0]
                dummy = curr = ListNode()

                while l1 and l2:
                    if l1.val < l2.val:
                        curr.next = l1
                        l1 = l1.next
                    else:
                        curr.next = l2
                        l2 = l2.next
                    curr = curr.next
                
                curr.next = l1 or l2
                return [dummy.next]
        
        return merge(lists[:len(lists) // 2], lists[len(lists) // 2:])[0]