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
                return merge(merge(lists1[:m // 2], lists1[m // 2:]), merge(lists2[:n // 2], lists2[n // 2:]))
            else:
                dummy = curr = ListNode()
                lists1, lists2 = lists1[0], lists2[0]
                while lists1 and lists2:
                    if lists1.val < lists2.val:
                        curr.next = lists1
                        lists1 = lists1.next
                    else:
                        curr.next = lists2
                        lists2 = lists2.next
                    curr = curr.next
                
                curr.next = lists1 or lists2

                return [dummy.next]
        
        return merge(lists[:len(lists) // 2], lists[len(lists) // 2:])[0]