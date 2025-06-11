# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return None
        slow = fast = head
        i=1

        # Move fast pointer to the (N-n)
        while i<=n:
            fast = fast.next
            i+=1
        
        if fast==None:
            return head.next
        
        # Loop fast till end so that slow reaches 1 node before nth node from end of list
        while (fast.next):
            slow=slow.next
            fast = fast.next
            
        # Removing nth node from end of list
        slow.next = slow.next.next

        return head
        



            
