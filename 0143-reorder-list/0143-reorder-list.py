# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Find middle node of LL
            # Slow and fast pointer approach
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of LL
            # In place reversal
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Link first element of first half to first element of second half
        first_half = head
        second_half = prev
        while second_half.next:
            temp1 = first_half.next
            first_half.next = second_half
            first_half = temp1
            temp2 = second_half.next
            second_half.next = first_half
            second_half = temp2
        
        return head