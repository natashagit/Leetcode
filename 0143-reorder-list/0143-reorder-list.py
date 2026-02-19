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
        # input: linked list L0->L1->L2->L3
        # output: ll L0->L3->L1->L2
        # divide into two #with slow and fast ptr
        # reverse second half
        # merge by taking every alternate element 
        
 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr

        first_half = head
        second_half = prev

        while second_half.next:
            temp1 = first_half.next
            first_half.next = second_half
            temp2 = second_half.next
            first_half  = temp1
            second_half.next = first_half
            second_half = temp2

        return head

