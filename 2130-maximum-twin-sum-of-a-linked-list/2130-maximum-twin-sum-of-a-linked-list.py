# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # input: even node linkedlist
        # output: max twin sum, where twins are nodes i, n-i-1
        # find midpt
        # 5 -> 4 -> 2 -> 1
        # reverse second half
        # 5 ->4 1-> 2
        # traverse through l1 and l2 -> take sum-> store max
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_ptr = slow.next
            slow.next = prev
            prev = slow
            slow = next_ptr
        l2 = prev
        l1 = head
        max_sum = 0
        while l2:
            max_sum = max(max_sum, l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
        return max_sum


