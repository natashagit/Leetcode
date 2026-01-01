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
        # input: LL
        # output: LL in order having first, last, second, second last element
        # edge case: empty list, one element

        # split the LL into two
        # reverse the second half
        # merge every element one by one from both lists

        # split into two
        # get midpoint of LL
        # use slow and fast pointer, slow ptr will be the midpoint
        # second half list starts at slow ptr
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half list
        # use prev=None
        # current pointing to slow
        # while current, set next ptr as current's next
        # set current's next to prev and prev to current and current to next ptr
        # prev will now be start of second half of list
        prev = None
        current = slow
        while current:
            next_ptr = current.next
            current.next = prev
            prev = current
            current = next_ptr
        second_half = prev

        # merge two lists
        # set first half of list to head
        # create dummy node and set to first half/head
        # save first half's next in temp1
        # first half's next saved as second half
        # second half's next in temp2
        # first half now set as temp1
        # second half's next saved as first half
        # second half now set as temp2
        first_half = head
        while second_half.next:
            temp1 = first_half.next
            first_half.next = second_half
            temp2 = second_half.next
            first_half = temp1
            second_half.next = first_half
            second_half = temp2

        # return dummy
        return head