# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # input: head of linked list
        # output: reversed linked list
        # keep a previous pointer as NULL
        # keep a current pointer at the head
        # do this while current lasts
        # have a NEXT pointer for the pointer after current
        # set the current's next to the previous pointer
        # set the current as the NEXT pointer
        # set the previous as current
        # return the previous 

        previous = None
        current = head
        while current:
            next_ptr = current.next
            current.next = previous
            previous = current
            current = next_ptr
        return previous
            
