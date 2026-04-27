# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 0 -> 1 -> 2 -> 3 <- 4 <- 5 <- 6 store head and reversed head (tail)
        # 0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3 -> 3 -> 3

        # 0 -> 1 -> 2 -> 3
        # 0 -> 1 -> 2 <- 3
        # 0 -> 3 -> 1 -> 2

        # while list1.next and list2.next:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            currNextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = currNextTemp

        list1, list2 = head, prev
        while list2:
            list1Temp, list2Temp = list1.next, list2.next
            list1.next, list2.next = list2, list1Temp
            list1, list2 = list1Temp, list2Temp




