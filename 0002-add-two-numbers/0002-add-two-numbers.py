# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # input: two ll
        # output: ll in reverse order of sum of the number formed by the digits in the reversed two lls
        # edge case: empty list
        
        # reverse l1 and l2 and keep count of length as n1 and n2
        # [3, 4, 2] [4, 6, 5] 3, 3
        # calculate sum by looping through ll and adding multiplied value of element with 10^(n1-1) and keep reducing n1
        # 342, 465 
        # Add the two sums
        # 807

        # Now while number exists
        # split number by taking mod by 10 and store in ll
        # keep updating number 

        def reverse(ll):
            prev = None
            curr = ll
            n=0
            while curr:
                n+=1
                next_ptr = curr.next
                curr.next = prev
                prev = curr
                curr = next_ptr
            return prev, n
        
        def calculate_sum(ll, n):
            result_sum = 0
            curr = ll
            while curr:
                result_sum += curr.val*((10)**n)
                n-=1
                curr = curr.next
            return result_sum
        
        rev_l1, n1 = reverse(l1)
        rev_l2, n2 = reverse(l2)

        final_sum = calculate_sum(rev_l1, n1-1)+calculate_sum(rev_l2, n2-1)
        dummy = ListNode(0)
        curr = dummy

        if final_sum == 0:
            return ListNode(0)

        while final_sum>0:
            rem = final_sum%10
            curr.next = ListNode(rem)
            curr = curr.next
            final_sum = final_sum//10
        
        return dummy.next
