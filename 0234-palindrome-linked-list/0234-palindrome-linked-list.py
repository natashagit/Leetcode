# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer to find the midpoint when fast reaches the end
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # Check if first half == second half :  then palindrome
        left, right = head, prev
        while left!=None and right!=None:
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        return True