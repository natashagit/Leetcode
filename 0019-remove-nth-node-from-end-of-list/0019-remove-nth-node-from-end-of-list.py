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
        fast = slow = head
        i = 1
        if fast==None:
            return None
            
        while(i<=n):
            fast = fast.next
            i+=1
        
        if fast==None:
            return head.next

        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next=slow.next.next

        return head
        
        