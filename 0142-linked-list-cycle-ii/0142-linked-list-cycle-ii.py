# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Consider edge case
        if head==None or head.next==None:
            return None
        slow = fast = head
        while (fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        else:
            # Situation when no cycle
            return None
        # When fast goes to next, it will be at head of cycle: as previously it was at the end of the list
        pointer = head
        while pointer!=fast:
            pointer = pointer.next
            fast = fast.next
        return pointer

