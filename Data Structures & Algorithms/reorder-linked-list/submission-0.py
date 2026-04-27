# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (head is None):
            return
        arr = []
        current = head
        length = 0
        while (current):
            arr.append(current)
            current = current.next
            length += 1
        start = 0
        end = length - 1
        last = head
        while (start < end):
            arr[start].next = arr[end]
            start += 1
            if (start == end):
                last = arr[start]
                break
            arr[end].next = arr[start]
            end -= 1
            last = arr[start]
        if (last is not None):
            last.next = None
