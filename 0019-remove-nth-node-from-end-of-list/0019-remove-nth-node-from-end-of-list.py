# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # input: ll and nth node from end of list to remove [1,2,3,4,5], 2
        # output: ll with n'th node from end removed [1,2,3,5]
        # edge cases: only one node, or empty list, or n more than length of ll

        # use slow and fast pointer
        # move fast pointer to nth node from start with a loop
        # start a slow pointer to move from start till the fast pointer reaches the end
        # slow pointer will reach a node before nth node from end

        slow = fast = head
        if slow is None or slow.next is None:
            return None
        i=0
        while i<n:
            fast = fast.next
            i+=1
        
        if fast is None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head

